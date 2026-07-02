# DevOps Production Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=github-actions)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?logo=amazon-aws)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-009639?logo=nginx)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana)
![Alertmanager](https://img.shields.io/badge/Alertmanager-Alerting-orange)
![Node_Exporter](https://img.shields.io/badge/Node_Exporter-System_Metrics-5A5A5A)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

# DevOps Production Platform

A production-style DevOps project that demonstrates how to build, containerize, monitor, alert on, and automate deployment workflows for a Flask backend using Docker, PostgreSQL, Prometheus, Alertmanager, Grafana, GitHub Actions, Terraform, Kubernetes, and AWS.

## Project Overview

This repository showcases practical DevOps skills across:

- application containerization
- infrastructure automation
- observability and alerting
- CI/CD automation
- cloud and Kubernetes deployment structure

The platform includes:

- a Flask backend application
- PostgreSQL as the application database
- Docker Compose for local multi-service orchestration
- Prometheus for metrics collection and alert evaluation
- Alertmanager for email notifications
- Grafana for dashboards and visualization
- Node Exporter for infrastructure metrics
- GitHub Actions for testing and Docker image publishing
- Terraform for infrastructure-as-code
- Kubernetes manifests for container orchestration deployment structure
- AWS support for cloud infrastructure workflows

## Architecture

The local stack contains the following services:

- **backend** – Flask application exposing application endpoints and Prometheus metrics
- **postgres** – PostgreSQL database for backend persistence
- **prometheus** – scrapes metrics and evaluates alert rules
- **alertmanager** – sends email notifications when alerts fire
- **grafana** – visualizes metrics and dashboards
- **node-exporter** – exposes infrastructure metrics

## Repository Structure

```text
.
├── .github/workflows/
│   └── ci-cd.yml
├── app/
│   └── backend/
├── docs/
│   └── screenshots/
├── kubernetes/
├── monitoring/
│   ├── alert.rules.yml
│   ├── alertmanager.yml
│   ├── prometheus.yml
│   ├── grafana/
│   │   ├── dashboards/
│   │   └── provisioning/
│   └── secrets/                  # local only, not committed
├── terraform/
├── docker-compose.yml
├── .env.example
├── LICENSE
└── README.md


Features
Containerized Flask backend with PostgreSQL
Local multi-container orchestration using Docker Compose
Monitoring with Prometheus
Email alerting with Alertmanager and Gmail SMTP
Dashboards with Grafana
Infrastructure metrics with Node Exporter
Automated testing and Docker image publishing with GitHub Actions
Terraform-ready infrastructure-as-code structure
Kubernetes manifest support
Public portfolio-ready DevOps project structure
Tech Stack
Backend: Flask, Python
Database: PostgreSQL
Containers: Docker, Docker Compose
Monitoring: Prometheus, Node Exporter
Alerting: Alertmanager, Gmail SMTP
Visualization: Grafana
CI/CD: GitHub Actions
Infrastructure as Code: Terraform
Container Orchestration: Kubernetes
Cloud: AWS
Prerequisites
Before running the project locally, ensure you have:

Docker
Docker Compose
Git
a Gmail account with:
2-Step Verification enabled
an App Password created for SMTP alerting
Local Setup
1. Clone the repository
bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
2. Create the environment file
Create a .env file in the project root:

env
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=devdb
Or copy from the example file:

bash
cp .env.example .env
3. Create the Alertmanager secret file
Create the Gmail App Password file used by Alertmanager:

bash
mkdir -p monitoring/secrets
echo "YOUR_GMAIL_APP_PASSWORD" > monitoring/secrets/gmail_app_password.txt
Use a Gmail App Password, not your normal Gmail account password.

4. Start the platform
bash
docker-compose up --build
Local Service URLs
Once the stack is running, you can access:

Flask backend: http://localhost:5000
Prometheus: http://localhost:9090
Alertmanager: http://localhost:9093
Grafana: http://localhost:3000
Node Exporter metrics: http://localhost:9100/metrics
Monitoring and Alerting
Prometheus is configured to scrape:

Flask backend metrics
Node Exporter metrics
Prometheus self-metrics
Alertmanager metrics
Alert rules include:

FlaskBackendDown
NodeExporterDown
PrometheusDown
AlertmanagerDown
HighCPUUsage
Alertmanager is configured to send email notifications using Gmail SMTP.

How to Test Alerts
To force a backend-down alert:

bash
docker stop flask-backend
Wait at least 1–2 minutes because the alert rule uses a for duration before entering the firing state.

Then verify:

Prometheus alerts page: http://localhost:9090/alerts
Alertmanager UI: http://localhost:9093
You should also receive an email notification.

To restore the backend:

bash
docker start flask-backend
If send_resolved: true is enabled in Alertmanager, you should also receive a recovery email.

Grafana
Grafana is included for dashboard visualization and observability.

Typical usage includes:

infrastructure monitoring dashboards
backend service health dashboards
Prometheus datasource integration
tracking metrics over time
Default local URL:

text
http://localhost:3000
If dashboards and datasources are provisioned through the monitoring/grafana/ directory, Grafana will load them automatically on startup.

CI/CD Pipeline
GitHub Actions is used to automate testing and Docker image publishing.

Workflow behavior
On:

push to main
pull requests targeting main
The pipeline:

starts a PostgreSQL service in GitHub Actions
installs Python dependencies
runs backend tests
builds the backend Docker image
pushes the image to Docker Hub on successful push to main
Required GitHub Secrets
To publish Docker images, configure these repository secrets:

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Terraform
The repository includes Terraform configuration for infrastructure-as-code workflows.

Typical Terraform usage may include:

provisioning AWS infrastructure
networking resources
compute resources
deployment support for application services
Do not commit real terraform.tfvars files or cloud credentials.

Kubernetes
The repository also includes Kubernetes manifests for deployment structure and orchestration practice.

These manifests may include resources such as:

deployments
services
ingress
configmaps
secrets
autoscaling configuration
persistent volume claims
If you use Kubernetes secrets, keep real values out of public repositories. Use example manifests or placeholders instead.

Screenshots
Add screenshots to strengthen the project presentation.

Recommended location:

text
docs/screenshots/
Recommended screenshots:

Prometheus targets
Prometheus alerts
Alertmanager UI
Grafana dashboard
received email alert
GitHub Actions successful workflow run
Prometheus Targets
Prometheus Targets

Prometheus Alerts
Prometheus Alerts

Alertmanager UI
Alertmanager UI

Grafana Dashboard
Grafana Dashboard

Email Alert
Email Alert

GitHub Actions Success
GitHub Actions Success

Security Notes
This repository is structured to avoid committing secrets.

Do not commit
.env
monitoring/secrets/gmail_app_password.txt
terraform.tfvars
cloud credentials
API keys
real SMTP passwords
real Kubernetes secret values
Secret handling used in this project
local environment variables are stored in .env
Gmail SMTP authentication uses a mounted local secret file
example configuration files are safe to commit
ignored files are managed through .gitignore
If any secret was ever accidentally committed, it should be rotated immediately.

Recommended Verification Steps
After setup, verify the following:

Backend
bash
curl http://localhost:5000
Prometheus targets
Open:

text
http://localhost:9090/targets
Ensure targets are up.

Alert rules
Open:

text
http://localhost:9090/rules
Alertmanager
Open:

text
http://localhost:9093
Grafana
Open:

text
http://localhost:3000
Useful Commands
Start services
bash
docker-compose up --build
Stop services
bash
docker-compose down
Rebuild and restart
bash
docker-compose down
docker-compose up --build
View Alertmanager logs
bash
docker logs alertmanager
Trigger a backend-down alert
bash
docker stop flask-backend
Restore backend
bash
docker start flask-backend
Skills Demonstrated
This project demonstrates:

Docker containerization
multi-service orchestration
service networking
environment and secret management basics
infrastructure monitoring
alerting and incident notification
dashboard visualization
CI/CD automation
Terraform project structure
Kubernetes deployment structure
portfolio-grade DevOps documentation
Future Improvements
Potential next enhancements:

add Nginx reverse proxy
add HTTPS/TLS
improve backend health checks
add memory, disk, and container restart alerts
add linting and security scanning to CI
add Terraform validation in CI
add full AWS deployment automation
add Kubernetes deployment guide
use managed secret stores in production environments
License
This project is licensed under the MIT License.

Author
Ibraheem Aloyinlapa

GitHub: Alibras257