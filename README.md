# DevOps Production Platform

[![CI/CD Pipeline](https://github.com/Alibras257/devops-production-platform/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Alibras257/devops-production-platform/actions/workflows/ci-cd.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![Terraform](https://img.shields.io/badge/Terraform-Validated-7B42BC.svg)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-EC2%20Deployment-FF9900.svg)](https://aws.amazon.com/ec2/)
[![Monitoring](https://img.shields.io/badge/Monitoring-Prometheus%20%7C%20Grafana-E6522C.svg)](#monitoring-and-alerting)

A production-style DevOps project that demonstrates how to build, containerize, test, scan, monitor, and automatically deploy a Flask application with PostgreSQL using Docker, Nginx, GitHub Actions, Terraform, Kubernetes manifests, Prometheus, Grafana, Alertmanager, Node Exporter, and AWS EC2.

---

## Highlights

- Containerized Flask + PostgreSQL application
- Nginx reverse proxy for local and production access
- Health and readiness endpoints for deployment reliability
- Prometheus, Grafana, Alertmanager, and Node Exporter integration
- CI/CD pipeline with linting, formatting, tests, dependency audit, Terraform validation, image scanning, and Docker image publishing
- Automated EC2 deployment from GitHub Actions over SSH
- Production deployment flow using Docker Compose
- Kubernetes manifests with readiness/liveness probes and autoscaling structure

---

## Architecture

### Application Flow

```text
Client
  |
  v
Nginx
  |
  v
Flask Backend
  |
  v
PostgreSQL
CI/CD Flow
text
Developer Push
   |
   v
GitHub Actions
   ├── Ruff / Black / Pytest / pip-audit
   ├── Terraform fmt / validate
   ├── Docker image build
   ├── Trivy image scan
   ├── Docker Hub push
   └── SSH deploy to AWS EC2
             |
             v
        Docker Compose (prod)
             |
             v
      Nginx + Flask + PostgreSQL
Monitoring Flow
text
Flask metrics ----\
Node Exporter -----\ 
Prometheus ---------> Grafana
Alert rules --------> Alertmanager ----> Email notifications
Repository Structure
text
.
├── .github/workflows/
│   └── ci-cd.yml
├── app/
│   └── backend/
│       ├── Dockerfile
│       ├── app.py
│       ├── init_db.py
│       ├── models.py
│       ├── routes.py
│       ├── extensions.py
│       ├── tests/
│       └── requirements.txt
├── deploy/
│   ├── deploy.sh
│   ├── ec2-bootstrap.sh
│   └── verify.sh
├── docs/
│   └── screenshots/
├── kubernetes/
├── monitoring/
│   ├── alert.rules.yml
│   ├── alertmanager.yml
│   ├── prometheus.yml
│   └── grafana/
├── nginx/
│   └── nginx.conf
├── terraform/
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
├── LICENSE
└── README.md
Tech Stack
Application
Python
Flask
PostgreSQL
SQLAlchemy
Gunicorn
Containers and Proxy
Docker
Docker Compose
Nginx
Monitoring and Alerting
Prometheus
Grafana
Alertmanager
Node Exporter
CI/CD and Security
GitHub Actions
Ruff
Black
pytest
pip-audit
Trivy
Docker Hub
Infrastructure and Cloud
Terraform
AWS EC2
Kubernetes manifests
Features
Containerized Flask backend with PostgreSQL
Nginx reverse proxy in front of the application
Local multi-container orchestration using Docker Compose
Production deployment using docker-compose.prod.yml
Health and readiness endpoints for application reliability
Docker health checks for backend and database services
Monitoring with Prometheus
Email alerting with Alertmanager and Gmail SMTP
Dashboards with Grafana
Infrastructure metrics with Node Exporter
Automated linting, formatting, dependency audit, and tests with GitHub Actions
Docker image vulnerability scanning with Trivy
Docker image publishing to Docker Hub
Automated EC2 deployment from GitHub Actions over SSH
Terraform validation in CI
Kubernetes manifests with readiness/liveness probes and autoscaling structure
Local Setup
Prerequisites
Install the following:

Docker
Docker Compose
Git
For Alertmanager email notifications, also prepare:

a Gmail account
2-Step Verification enabled
a Gmail App Password
1. Clone the repository
bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
2. Create the environment file
bash
cp .env.example .env
Example:

env
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=devdb
3. Create the Alertmanager secret file
bash
mkdir -p monitoring/secrets
echo "YOUR_GMAIL_APP_PASSWORD" > monitoring/secrets/gmail_app_password.txt
4. Start the local stack
bash
docker-compose up --build
Local Service URLs
After startup:

Application: http://localhost:8080
Health check: http://localhost:8080/health
Readiness check: http://localhost:8080/ready
Prometheus: http://localhost:9090
Alertmanager: http://localhost:9093
Grafana: http://localhost:3000
Node Exporter metrics: http://localhost:9100/metrics
Health and Readiness Checks
The backend exposes:

/health → confirms the app process is alive
/ready → confirms the app can reach PostgreSQL
These endpoints are used for:

Docker health checks
Kubernetes readiness/liveness probes
deployment verification
Example:

bash
curl http://localhost:8080/health
curl http://localhost:8080/ready
Monitoring and Alerting
Prometheus is configured to scrape metrics from:

Flask backend
Node Exporter
Prometheus
Alertmanager
Alerting examples include:

backend down
Node Exporter down
Prometheus down
Alertmanager down
high CPU usage
Alertmanager is configured to send notifications through Gmail SMTP.

Test an alert locally
bash
docker stop flask-backend
Wait 1–2 minutes, then verify:

http://localhost:9090/alerts
http://localhost:9093
Restore the backend:

bash
docker start flask-backend
CI/CD Pipeline
GitHub Actions automates the delivery pipeline.

Pipeline stages
On push to main and pull requests targeting main, the workflow runs:

Lint, format, audit, and test

Ruff
Black
pip-audit
pytest
Terraform validation

terraform fmt -check
terraform init -backend=false
terraform validate
Docker image security scan

Docker build
Trivy scan
Docker image publish

build backend image
push image to Docker Hub on successful push to main
Automated EC2 deployment

connect to EC2 over SSH
pull latest image
redeploy containers
verify /health and /ready
Required GitHub Secrets
Docker Hub
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
EC2 Deployment
EC2_HOST
EC2_USER
EC2_SSH_KEY
EC2_APP_DIR
Production Deployment on EC2
The project supports production-style deployment to AWS EC2 using docker-compose.prod.yml.

First-time server bootstrap
bash
bash deploy/ec2-bootstrap.sh
This installs:

Docker Engine
Docker Compose plugin
Create .env on EC2
Example:

env
DOCKERHUB_USERNAME=yourdockerhubusername
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=devdb
Initialize the database once
bash
docker compose -f docker-compose.prod.yml down -v
docker compose -f docker-compose.prod.yml up -d postgres
docker compose -f docker-compose.prod.yml run --rm backend python init_db.py
Start the production stack
bash
docker compose -f docker-compose.prod.yml up -d
Verify deployment
bash
bash deploy/verify.sh
Deployment Scripts
deploy/ec2-bootstrap.sh
Bootstraps an EC2 instance with Docker and Docker Compose.

deploy/deploy.sh
Pulls the latest images and starts the production stack.

deploy/verify.sh
Checks the deployed application using /health and /ready.

app/backend/init_db.py
Runs one-time database initialization outside Gunicorn startup to avoid multi-worker race conditions.

Kubernetes
The repository includes Kubernetes manifests for deployment structure and orchestration practice, including:

namespace
backend deployment
backend service
PostgreSQL deployment
PostgreSQL service
persistent volume claim
configmap
secret example
ingress
horizontal pod autoscaler
The backend deployment includes:

readiness probe
liveness probe
resource requests and limits
Terraform
The Terraform configuration currently supports:

formatting checks
initialization without backend
validation in CI
The Terraform directory is structured for future AWS infrastructure provisioning enhancements.

Screenshots
Screenshots are stored in:

text
docs/screenshots/
Suggested visuals include:

Prometheus targets
Prometheus alerts
Alertmanager UI
Grafana dashboard
email alert examples
GitHub Actions successful workflow runs
Useful Commands
Start local stack
bash
docker-compose up --build
Stop local stack
bash
docker-compose down
Rebuild local stack
bash
docker-compose down
docker-compose up --build
Check local health
bash
curl http://localhost:8080/health
curl http://localhost:8080/ready

Start production stack
bash
docker compose -f docker-compose.prod.yml up -d
Pull latest production images
bash
docker compose -f docker-compose.prod.yml pull
Run DB initialization
bash
docker compose -f docker-compose.prod.yml run --rm backend python init_db.py
Verify production deployment
bash
bash deploy/verify.sh
Security Notes
This repository is structured to avoid committing secrets.

Do not commit:

.env
monitoring/secrets/gmail_app_password.txt
cloud credentials
API keys
real SMTP passwords
real Kubernetes secret values
private SSH keys
Recommended secret handling:

local environment variables in .env
GitHub Actions secrets for CI/CD
server-side .env on EC2
example secret files only in version control
If any secret is exposed, rotate it immediately.

Skills Demonstrated
This project demonstrates:

Docker containerization
reverse proxy configuration
multi-service orchestration
health and readiness checks
environment and secret handling
monitoring and observability
alerting and notification workflows
CI/CD pipeline design
container image security scanning
Infrastructure as Code validation
EC2 deployment automation
deployment troubleshooting
Kubernetes deployment structure
Future Improvements
Potential next enhancements:

HTTPS/TLS with Nginx and Let's Encrypt
Flask-Migrate / Alembic for schema migrations
full Terraform-based AWS infrastructure provisioning
remote Terraform state management
staging and production environment separation
AWS SSM Parameter Store or Secrets Manager integration
Kubernetes deployment to a live cluster such as EKS
blue/green or rolling deployment strategy
centralized log aggregation
License
This project is licensed under the MIT License.

Author
Ibraheem Aloyinlapa

GitHub: Alibras257