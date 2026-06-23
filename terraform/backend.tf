terraform {
  backend "s3" {
    bucket         = "alibras257-devops-production-tf-state"
    key            = "devops-production-platform/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
