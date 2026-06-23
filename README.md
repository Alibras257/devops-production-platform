# DevOps Production Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=github-actions)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A production-style DevOps platform that demonstrates how to build, test, containerize, and deploy a backend application using Flask, PostgreSQL, Docker, Kubernetes, Terraform, GitHub Actions, and AWS.

---

## Project Overview

This project is a backend-focused DevOps platform built with Flask and PostgreSQL, packaged with Docker, validated through automated testing, and integrated with a CI/CD pipeline using GitHub Actions.

The platform also includes Terraform-based AWS infrastructure provisioning and automated EC2 deployment using `user_data` to install Docker and run the application container at launch.

The purpose of this project is to demonstrate practical DevOps, cloud, and platform engineering skills, including:

- application containerization
- multi-service orchestration with Docker Compose
- backend service testing and validation
- CI/CD workflow automation with GitHub Actions
- Kubernetes deployment configuration
- infrastructure provisioning with Terraform
- automated cloud deployment on AWS EC2

---

## Features

- Flask backend application
- PostgreSQL database integration
- Dockerized application setup
- Docker Compose for local multi-container development
- Automated testing with `pytest`
- GitHub Actions CI/CD pipeline
- Docker Hub image build and push automation
- Kubernetes deployment and service manifests
- Terraform infrastructure provisioning for AWS
- Automated EC2 bootstrapping with Terraform `user_data`
- Public cloud deployment on AWS EC2
- Docker image pulled and deployed automatically on instance launch
- Clean project structure for portfolio and production-style presentation

---

## Tech Stack

- **Backend:** Flask
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Orchestration:** Docker Compose, Kubernetes
- **CI/CD:** GitHub Actions
- **Infrastructure as Code:** Terraform
- **Cloud Platform:** AWS EC2, Render
- **Testing:** Pytest

---

## Repository Structure

```text
devops-production-platform/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   └── backend/
│       ├── app.py
│       ├── config.py
│       ├── extensions.py
│       ├── models.py
│       ├── routes.py
│       ├── utils.py
│       ├── requirements.txt
│       ├── tests/
│       │   └── test_app.py
│       └── __init__.py
├── docker/
│   └── Dockerfile
├── kubernetes/
│   ├── backend-deployment.yml
│   └── backend-service.yml
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── main.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
├── monitoring/
├── docs/
├── scripts/
├── docker-compose.yml
├── README.md
└── .gitignore
Architecture Diagram
text
                        +----------------------+
                        |    GitHub Repository |
                        | Source Code & Config |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        | GitHub Actions CI/CD |
                        | - Install deps       |
                        | - Run tests          |
                        | - Start PostgreSQL   |
                        | - Build Docker image |
                        | - Push to Docker Hub |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |     Docker Hub       |
                        |   Backend Image      |
                        +----------+-----------+
                                   |
                                   v
                 +---------------------------------------------+
                 | Terraform-Provisioned AWS Infrastructure    |
                 | - VPC                                       |
                 | - Public Subnet                             |
                 | - Internet Gateway                          |
                 | - Route Table                               |
                 | - Security Group                            |
                 | - EC2 Instance                              |
                 +-------------------+-------------------------+
                                     |
                                     v
                        +----------------------+
                        |      EC2 Instance    |
                        |  Docker via user_data|
                        |  Runs Flask Backend  |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |   Public App Access  |
                        |   Port 5000 on EC2   |
                        +----------------------+
CI/CD Workflow
The GitHub Actions pipeline automates the following:

checks out the repository
sets up Python
installs dependencies
starts a PostgreSQL service for testing
runs automated tests with pytest
builds the backend Docker image
pushes the image to Docker Hub after successful validation
Workflow file:

text
.github/workflows/ci-cd.yml
AWS Infrastructure Provisioning
The project uses Terraform to provision AWS infrastructure for deployment. The infrastructure includes:

a custom VPC
a public subnet
an internet gateway
a route table and route table association
a security group for SSH, HTTP, and application traffic
an EC2 instance for application hosting
Terraform also uses EC2 user_data to automate instance bootstrapping by:

installing Docker
enabling and starting the Docker service
pulling the application image from Docker Hub
running the Flask backend container automatically on launch
How It Works
Code is pushed to GitHub.
GitHub Actions triggers the CI/CD pipeline automatically.
The backend application is tested using PostgreSQL and pytest.
The Docker image is built and pushed to Docker Hub.
Terraform provisions AWS infrastructure for deployment.
The EC2 instance launches and runs bootstrap commands through user_data.
Docker is installed automatically on the instance.
The backend image is pulled from Docker Hub and started automatically.
The application becomes publicly accessible through the EC2 public IP.
Installation and Setup
1. Clone the repository
bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
2. Set up environment variables
Create a .env file if needed for local development and configure your database connection settings.

3. Install backend dependencies
bash
pip install -r app/backend/requirements.txt
4. Run the backend locally
bash
cd app/backend
python app.py
The app should be available at:

text
http://localhost:5000
Run with Docker
Build the Docker image
bash
docker build -t flask-backend ./app/backend
Run the container
bash
docker run -p 5000:5000 flask-backend
Run with Docker Compose
To start the backend and PostgreSQL together:

bash
docker-compose up --build
To stop the services:

bash
docker-compose down
Running Tests
Run tests locally with:

bash
pytest app/backend/tests -v
Terraform Usage
To provision the AWS infrastructure:

bash
cd terraform
terraform init
terraform validate
terraform plan
terraform apply
Terraform outputs the public IP of the EC2 instance after successful deployment.

To replace the EC2 instance and re-run automated provisioning:

bash
terraform apply -replace="aws_instance.devops_server"
Deployment
This project supports multiple deployment approaches, including local containerized development, cloud deployment, and infrastructure automation.

Current deployment targets include:

Render for managed cloud hosting
AWS EC2 provisioned with Terraform for infrastructure-level deployment
The AWS deployment uses Terraform to provision infrastructure and EC2 user_data to install Docker and start the backend container automatically.

Current AWS Demo Endpoint
text
http://18.213.111.78:5000/
Note: This public IP may change if the EC2 instance is replaced or recreated.

Kubernetes Deployment
Kubernetes manifests are included for backend deployment and service exposure.

Apply them with:

bash
kubectl apply -f kubernetes/
Included manifests:

backend-deployment.yml
backend-service.yml
API Endpoint
Current backend test endpoint:

/ — application status / backend response
Example response:

json
{"status":"connected to app layer"}
Why This Project Matters
This project highlights essential DevOps and cloud engineering skills in a practical, portfolio-ready format:

containerizing backend applications with Docker
integrating application and database services
automating testing and validation in CI/CD
provisioning cloud infrastructure with Terraform
automating EC2 configuration with user_data
deploying containerized applications to AWS
preparing services for Kubernetes-based deployment
maintaining a clean and reproducible development workflow
It is suitable for showcasing DevOps, Cloud, Platform Engineering, SRE, and Backend engineering capabilities.

Future Improvements
Potential next enhancements:

configure remote Terraform state with S3 and DynamoDB
add Nginx reverse proxy on port 80
add HTTPS and domain configuration
integrate Prometheus and Grafana monitoring
package Kubernetes resources with Helm
implement GitOps with Argo CD
expand automated test coverage
deploy to a managed Kubernetes service such as EKS
Author
Ibraheem Aloyinlapa
GitHub: Alibras257

License
This project is for educational and portfolio purposes.