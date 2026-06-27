output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.devops_vpc.id
}

output "subnet_a_id" {
  description = "ID of public subnet A"
  value       = aws_subnet.public_subnet_a.id
}

output "subnet_b_id" {
  description = "ID of public subnet B"
  value       = aws_subnet.public_subnet_b.id
}

output "security_group_id" {
  description = "ID of the application security group"
  value       = aws_security_group.devops_sg.id
}

output "rds_security_group_id" {
  description = "ID of the RDS security group"
  value       = aws_security_group.rds_sg.id
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.devops_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.devops_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.devops_server.public_dns
}

output "rds_endpoint" {
  description = "RDS PostgreSQL endpoint"
  value       = aws_db_instance.devops_postgres.address
}

output "rds_db_name" {
  description = "RDS database name"
  value       = aws_db_instance.devops_postgres.db_name
}