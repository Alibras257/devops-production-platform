# DevOps Production Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=github-actions)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana)
![Alertmanager](https://img.shields.io/badge/Alertmanager-Alerting-orange)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-009639?logo=nginx)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A production-style DevOps project that demonstrates application development, containerization, CI/CD, infrastructure provisioning, Kubernetes deployment, monitoring, and alerting using Flask, PostgreSQL, Docker, GitHub Actions, Terraform, AWS, Prometheus, Grafana, Alertmanager, and Nginx.

---

## Project Overview

This project is a backend-focused DevOps platform built with Flask and PostgreSQL. It is containerized with Docker, orchestrated locally with Docker Compose, provisioned in AWS using Terraform, and prepared for Kubernetes deployment with supporting manifests.

The platform also includes observability components such as Prometheus, Grafana, and Alertmanager, along with a CI/CD workflow using GitHub Actions.

This repository is designed to showcase practical skills in:

- backend application deployment
- containerization with Docker
- multi-service local orchestration with Docker Compose
- CI/CD pipeline automation
- Kubernetes-based deployment configuration
- infrastructure as code with Terraform
- AWS EC2 provisioning
- reverse proxying with Nginx
- monitoring and alerting with Prometheus, Grafana, and Alertmanager

---

## Features

- Flask backend service
- PostgreSQL database integration
- Dockerized backend application
- Docker Compose for local development
- Automated testing with `pytest`
- GitHub Actions CI/CD workflow
- Docker image build and push automation
- Kubernetes manifests for deployment and service exposure
- Horizontal Pod Autoscaler configuration
- Kubernetes ConfigMap and Secret configuration
- Terraform-based AWS infrastructure provisioning
- EC2 bootstrapping with `user_data`
- Nginx reverse proxy setup
- Prometheus metrics scraping
- Grafana dashboard provisioning
- Alertmanager configuration and alert rules
- Portfolio-ready project structure

---

## Tech Stack

- **Backend:** Flask
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Local Orchestration:** Docker Compose
- **Container Orchestration:** Kubernetes
- **CI/CD:** GitHub Actions
- **Infrastructure as Code:** Terraform
- **Cloud Platform:** AWS
- **Reverse Proxy:** Nginx
- **Monitoring:** Prometheus, Grafana
- **Alerting:** Alertmanager
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
│       ├── .dockerignore
│       ├── Dockerfile
│       ├── README.md
│       ├── __init__.py
│       ├── app.py
│       ├── config.py
│       ├── extensions.py
│       ├── models.py
│       ├── requirements.txt
│       ├── routes.py
│       ├── utils.py
│       └── tests/
├── docker/
├── docs/
├── kubernetes/
│   ├── backend-deployment.yml
│   ├── backend-service.yml
│   ├── configmap.yml
│   ├── hpa.yml
│   ├── ingress.yml
│   ├── namespace.yml
│   ├── postgres-deployment.yml
│   ├── postgres-pvc.yml
│   ├── postgres-service.yml
│   └── secret.yml
├── monitoring/
│   ├── alert.rules.yml
│   ├── alertmanager.yml
│   ├── grafana/
│   │   ├── dashboards/
│   │   └── provisioning/
│   └── prometheus.yml
├── scripts/
├── terraform/
│   ├── bootstrap/
│   │   ├── .terraform.lock.hcl
│   │   └── main.tf
│   ├── .terraform.lock.hcl
│   ├── backend.tf
│   ├── main.tf
│   ├── outputs.tf
│   ├── provider.tf
│   ├── terraform.tfvar
│   ├── terraform.tfvars.example
│   └── variables.tf
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
Architecture Summary
This project follows a production-style workflow:

Developers push code to GitHub.
GitHub Actions runs CI checks such as dependency installation, testing, and image build steps.
Docker images can be built and pushed to a container registry.
Terraform provisions AWS infrastructure for deployment.
EC2 instances can be bootstrapped automatically using user_data.
Nginx can be used as a reverse proxy in front of the Flask backend.
Prometheus scrapes application and infrastructure metrics.
Grafana visualizes those metrics through dashboards.
Alertmanager processes configured alerts.
CI/CD Workflow
The GitHub Actions workflow is intended to automate the following tasks:

check out repository code
set up the runtime environment
install dependencies
run automated tests
build the backend Docker image
optionally push the image to a registry
prepare for deployment workflows
Workflow file:

text
.github/workflows/ci-cd.yml
Infrastructure Provisioning
Terraform is used to provision AWS infrastructure for deployment.

Depending on the Terraform configuration in this repository, infrastructure may include:

networking components
security groups
compute instances
remote state configuration
bootstrap resources for Terraform backend setup
Main Terraform files:

text
terraform/
terraform/bootstrap/
Typical Terraform workflow:

bash
cd terraform
terraform init
terraform validate
terraform plan
terraform apply
If you are using bootstrap resources for remote state:

bash
cd terraform/bootstrap
terraform init
terraform plan
terraform apply
Kubernetes Deployment
Kubernetes manifests are included for deploying the application and supporting services.

Included resources currently cover:

namespace
backend deployment
backend service
ingress
ConfigMap
Secret
Horizontal Pod Autoscaler
PostgreSQL deployment
PostgreSQL service
PostgreSQL persistent volume claim
Apply all manifests with:

bash
kubectl apply -f kubernetes/
Monitoring and Alerting
The monitoring stack includes:

Prometheus for metrics scraping
Grafana for dashboards and visualization
Alertmanager for alert routing and handling
The repository also includes Prometheus alert rules and Grafana provisioning files.

Monitoring files
text
monitoring/prometheus.yml
monitoring/alert.rules.yml
monitoring/alertmanager.yml
monitoring/grafana/
Example local endpoints
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Alertmanager: http://localhost:9093
Default Grafana login
text
Username: admin
Password: admin
Change default credentials before using this in any real environment.

Local Development Setup
1. Clone the repository
bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
2. Install backend dependencies
bash
pip install -r app/backend/requirements.txt
3. Run the backend locally
bash
cd app/backend
python app.py
The application should be available at:

text
http://localhost:5000
Run with Docker
Build the backend image:

bash
docker build -t flask-backend ./app/backend
Run the container:

bash
docker run -p 5000:5000 flask-backend
Run with Docker Compose
To start the local stack:

bash
docker compose up --build
To stop the services:

bash
docker compose down
If your environment still uses the legacy command, docker-compose up --build will also work.

Running Tests
Run tests locally with:

bash
pytest app/backend/tests -v
Deployment Notes
This project supports multiple deployment-oriented workflows, including:

local containerized development
AWS infrastructure provisioning with Terraform
Kubernetes-based deployment using manifests
If your Terraform configuration provisions an EC2 instance, the backend can be started automatically through EC2 bootstrap logic such as user_data, and Nginx can be configured as a reverse proxy for public access.

Example public access pattern:

text
http://EC2_PUBLIC_IP
Example internal backend binding:

text
127.0.0.1:5000
API Endpoints
Current backend endpoints are expected to include:

/ — application status
/users — list or create users
/users/<id> — retrieve or update a user
/metrics — Prometheus metrics endpoint
Example status response:

json
{"status":"connected to app layer"}
Why This Project Matters
This project is useful as a portfolio and learning project because it demonstrates how to:

build and containerize a backend application
integrate application and database services
automate testing in CI/CD
provision cloud infrastructure with Terraform
prepare workloads for Kubernetes deployment
introduce observability with Prometheus and Grafana
add alerting with Alertmanager
organize a clean, production-style DevOps repository
It is suitable for showcasing skills relevant to:

DevOps Engineering
Cloud Engineering
Platform Engineering
Site Reliability Engineering
Backend Engineering
Future Improvements
Potential next enhancements include:

add HTTPS and domain configuration
integrate external alert receivers such as Slack or email
improve secrets management
add multi-environment deployment support
package Kubernetes resources with Helm
implement GitOps with Argo CD
expand automated test coverage
deploy to a managed Kubernetes platform such as EKS
add vulnerability scanning for containers and infrastructure
Screenshots
Add screenshots or architecture diagrams in the docs/ folder and reference them here.

Example:

md
![Architecture](docs/architecture.png)
Author
Ibraheem Aloyinlapa
GitHub: Alibras257

License
This project is for educational and portfolio purposes.