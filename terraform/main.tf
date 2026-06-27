resource "aws_vpc" "devops_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "devops-production-vpc"
  }
}

resource "aws_subnet" "public_subnet_a" {
  vpc_id                  = aws_vpc.devops_vpc.id
  cidr_block              = var.subnet_cidr
  availability_zone       = var.availability_zone
  map_public_ip_on_launch = true

  tags = {
    Name = "devops-production-public-subnet-a"
  }
}

resource "aws_subnet" "public_subnet_b" {
  vpc_id                  = aws_vpc.devops_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "devops-production-public-subnet-b"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.devops_vpc.id

  tags = {
    Name = "devops-production-igw"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.devops_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "devops-production-public-rt"
  }
}

resource "aws_route_table_association" "public_assoc_a" {
  subnet_id      = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_assoc_b" {
  subnet_id      = aws_subnet.public_subnet_b.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_security_group" "devops_sg" {
  name        = "devops-production-sg"
  description = "Allow restricted SSH and HTTP traffic"
  vpc_id      = aws_vpc.devops_vpc.id

  ingress {
    description = "SSH from trusted IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.trusted_ssh_cidr]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devops-production-sg"
  }
}

resource "aws_security_group" "rds_sg" {
  name        = "devops-production-rds-sg"
  description = "Allow PostgreSQL access from application server"
  vpc_id      = aws_vpc.devops_vpc.id

  ingress {
    description     = "PostgreSQL from EC2 security group"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.devops_sg.id]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devops-production-rds-sg"
  }
}

resource "aws_db_subnet_group" "devops_db_subnet_group" {
  name = "devops-production-db-subnet-group"
  subnet_ids = [
    aws_subnet.public_subnet_a.id,
    aws_subnet.public_subnet_b.id
  ]

  tags = {
    Name = "devops-production-db-subnet-group"
  }
}

resource "aws_db_instance" "devops_postgres" {
  identifier             = "devops-production-postgres"
  engine                 = "postgres"
  engine_version         = "16.3"
  instance_class         = var.db_instance_class
  allocated_storage      = 20
  db_name                = var.db_name
  username               = var.db_username
  password               = var.db_password
  publicly_accessible    = false
  skip_final_snapshot    = true
  deletion_protection    = false
  multi_az               = false
  storage_encrypted      = true
  db_subnet_group_name   = aws_db_subnet_group.devops_db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "devops-production-postgres"
  }
}

resource "aws_instance" "devops_server" {
  ami                         = var.ami_id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public_subnet_a.id
  vpc_security_group_ids      = [aws_security_group.devops_sg.id]
  associate_public_ip_address = true
  key_name                    = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              set -euxo pipefail

              yum update -y
              amazon-linux-extras install docker -y
              amazon-linux-extras install nginx1 -y

              systemctl enable docker
              systemctl start docker

              systemctl enable nginx
              systemctl start nginx

              usermod -aG docker ec2-user

              sleep 10

              docker rm -f flask-backend || true
              docker pull alibras257/flask-backend:latest
              docker run -d \
                --restart always \
                --name flask-backend \
                -p 127.0.0.1:5000:5000 \
                -e DATABASE_URL='postgresql://${var.db_username}:${var.db_password}@${aws_db_instance.devops_postgres.address}:5432/${var.db_name}' \
                alibras257/flask-backend:latest

              cat > /etc/nginx/nginx.conf <<'EONGINX'
              user nginx;
              worker_processes auto;
              error_log /var/log/nginx/error.log;
              pid /run/nginx.pid;

              events {
                  worker_connections 1024;
              }

              http {
                  include       /etc/nginx/mime.types;
                  default_type  application/octet-stream;

                  sendfile        on;
                  keepalive_timeout 65;

                  server {
                      listen 80;
                      server_name _;

                      location / {
                          proxy_pass http://127.0.0.1:5000;
                          proxy_set_header Host $host;
                          proxy_set_header X-Real-IP $remote_addr;
                          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                          proxy_set_header X-Forwarded-Proto $scheme;
                      }
                  }
              }
              EONGINX

              nginx -t
              systemctl restart nginx
              EOF

  tags = {
    Name = "devops-production-server"
  }

  depends_on = [aws_db_instance.devops_postgres]
}