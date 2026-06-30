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

A production-style DevOps project that demonstrates how to build, containerize, monitor, alert on, and automate deployment workflows for a Flask backend using Docker, PostgreSQL, Prometheus, Alertmanager, Grafana, GitHub Actions, Terraform, and AWS.

## Project Overview

This repository is designed to showcase practical DevOps skills across application packaging, infrastructure automation, observability, and CI/CD.

The platform includes:

- A Flask backend application
- PostgreSQL as the application database
- Docker Compose for multi-service local orchestration
- Prometheus for metrics scraping and alert evaluation
- Alertmanager for email notifications
- Grafana for dashboards and visualization
- Node Exporter for infrastructure metrics
- GitHub Actions for CI/CD automation
- Terraform for infrastructure-as-code
- AWS integration for cloud deployment workflows

## Architecture

The local platform is composed of the following services:

- **backend** – Flask application exposing application endpoints and Prometheus metrics
- **postgres** – PostgreSQL database for backend persistence
- **prometheus** – scrapes metrics and evaluates alert rules
- **alertmanager** – sends email notifications when alerts fire
- **grafana** – visualizes metrics and dashboards
- **node-exporter** – exposes system metrics for infrastructure monitoring

## Repository Structure

```text
.
├── .github/workflows/
│   └── ci-cd.yml
├── app/
│   └── backend/
├── monitoring/
│   ├── alert.rules.yml
│   ├── alertmanager.yml
│   ├── prometheus.yml
│   ├── grafana/
│   │   ├── dashboards/
│   │   └── provisioning/
│   └── secrets/            # local only, not committed
├── terraform/
├── docker-compose.yml
├── .env.example
└── README.md
Features
Containerized Flask backend with PostgreSQL
Local multi-container orchestration using Docker Compose
Metrics collection with Prometheus
Email alerting with Alertmanager and Gmail SMTP
Dashboards with Grafana
Infrastructure monitoring with Node Exporter
Automated testing and Docker image publishing with GitHub Actions
Terraform-based infrastructure provisioning support
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
Cloud: AWS
Prerequisites
Before running the project locally, ensure you have:

Docker
Docker Compose
Git
A Gmail account with:
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
You can also copy from the example file:

bash
cp .env.example .env
3. Create the Alertmanager secret file
Create the Gmail App Password file used by Alertmanager:

bash
mkdir -p monitoring/secrets
echo "YOUR_GMAIL_APP_PASSWORD" > monitoring/secrets/gmail_app_password.txt
Use a Gmail App Password, not your regular Gmail account password.

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
Prometheus scrape targets
Prometheus is configured to scrape:

Flask backend metrics
Node Exporter metrics
Prometheus self-metrics
Alertmanager metrics
Alert rules
The platform includes alerts such as:

FlaskBackendDown
NodeExporterDown
PrometheusDown
AlertmanagerDown
HighCPUUsage
Alert delivery
Alertmanager sends email notifications using Gmail SMTP.

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
If send_resolved: true is enabled in Alertmanager, you should also receive a recovery email when the service comes back up.

Grafana
Grafana is included for dashboard visualization.

Typical usage includes:

infrastructure monitoring dashboards
application health dashboards
Prometheus datasource integration
viewing metrics over time for CPU and service availability
Default local URL:

text
http://localhost:3000
If you provision dashboards and datasources through the monitoring/grafana/ directory, Grafana will automatically load them on startup.

CI/CD Pipeline
GitHub Actions is used to automate testing and Docker image builds.

Workflow behavior
On:

push to main
pull requests targeting main
The workflow:

Starts a PostgreSQL service in GitHub Actions
Installs Python dependencies
Runs backend tests
Builds the backend Docker image
Pushes the image to Docker Hub on successful push to main
Expected GitHub Secrets
To publish Docker images, configure these repository secrets:

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
Terraform
The repository includes a Terraform directory for infrastructure-as-code workflows.

Typical Terraform usage may include:

provisioning AWS infrastructure
networking and compute resources
deployment support for the application stack
Do not commit real terraform.tfvars files or cloud secrets.

Security Notes
This repository is structured to avoid committing secrets.

Secrets that should never be committed
.env
monitoring/secrets/gmail_app_password.txt
terraform.tfvars
cloud credentials
API keys or SMTP passwords
Secret handling used in this project
local environment variables are stored in .env
Gmail SMTP password is mounted from a local secret file
ignored files are managed through .gitignore
If a secret was ever accidentally committed, it should be rotated immediately.

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
Stop backend to trigger alert
bash
docker stop flask-backend
Start backend again
bash
docker start flask-backend
Screenshots
You can strengthen this project further by adding screenshots such as:

Prometheus targets page
Prometheus alerts page
Alertmanager active alerts
Grafana dashboard
received email alert
GitHub Actions successful workflow run
You can place them in a folder such as:

text
docs/screenshots/
Skills Demonstrated
This project demonstrates:

Docker containerization
multi-service orchestration
service networking
secret management basics
metrics collection and observability
alerting and incident notification
CI/CD automation
infrastructure-as-code structure
DevOps portfolio project organization
Future Improvements
Potential next enhancements:

add Nginx reverse proxy
add HTTPS with TLS
improve backend health checks
add memory, disk, and container restart alerts
add linting and security scanning to CI
add Terraform validation in CI
deploy the stack to AWS
add Kubernetes manifests or Helm charts
use managed secret stores for production
License
Add a license file if you want others to reuse or reference your project more formally.

Author
Ali Bras

GitHub: Alibras257