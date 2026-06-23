output "vpc_id" {
  value = aws_vpc.devops_vpc.id
}

output "subnet_id" {
  value = aws_subnet.public_subnet.id
}

output "security_group_id" {
  value = aws_security_group.devops_sg.id
}

output "instance_public_ip" {
  value = aws_instance.devops_server.public_ip
}
