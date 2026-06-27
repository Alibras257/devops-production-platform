variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment name"
  type        = string
  default     = "production"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
  description = "CIDR block for public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "availability_zone" {
  description = "Availability zone"
  type        = string
  default     = "us-east-1a"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "Amazon Machine Image ID"
  type        = string
  default     = "ami-0c02fb55956c7d316"
}

variable "key_name" {
  description = "SSH key pair name"
  type        = string
}

variable "trusted_ssh_cidr" {
  description = "Trusted CIDR block allowed to SSH into the EC2 instance"
  type        = string
}

variable "database_url" {
  description = "Database connection URL for the backend application"
  type        = string
  sensitive   = true
}