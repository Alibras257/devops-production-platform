# 🚀 DevOps Production Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?logo=kubernetes)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=githubactions)

A production-style DevOps project demonstrating a containerized Flask REST API with PostgreSQL, automated testing, Docker, Kubernetes, and GitHub Actions CI/CD.

---

# 🌐 Live Demo

**Application**

https://devops-production-platform.onrender.com

Example response:

```json
{
  "status": "connected to app layer"
}
```

---

# 📌 Project Overview

This project demonstrates an end-to-end DevOps workflow by taking a Python Flask application from local development through automated testing, containerization, orchestration, and deployment.

The project showcases:

* REST API development
* PostgreSQL database integration
* Docker containerization
* Kubernetes deployment
* GitHub Actions CI/CD
* Automated testing using Pytest
* Cloud deployment on Render

---

# 🏗️ Architecture

```text
                  GitHub Repository
                         │
                         ▼
                GitHub Actions CI/CD
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
     Run Pytest                  Build Docker Image
                                         │
                                         ▼
                                  Push to Docker Hub
                                         │
                                         ▼
                                  Kubernetes Cluster
                                         │
                                         ▼
                                 Flask REST API
                                         │
                                         ▼
                                   PostgreSQL
```

---

# ⚙️ Technology Stack

| Category         | Technology     |
| ---------------- | -------------- |
| Language         | Python 3.12    |
| Framework        | Flask          |
| Database         | PostgreSQL     |
| ORM              | SQLAlchemy     |
| Containerization | Docker         |
| Orchestration    | Kubernetes     |
| CI/CD            | GitHub Actions |
| Testing          | Pytest         |
| Version Control  | Git & GitHub   |
| Deployment       | Render         |

---

# 📂 Project Structure

```text
devops-production-platform/
│
├── app/
│   └── backend/
│       ├── app.py
│       ├── models.py
│       ├── extensions.py
│       ├── requirements.txt
│       ├── Dockerfile
│       └── tests/
│           └── test_app.py
│
├── kubernetes/
│   ├── backend-deployment.yml
│   └── backend-service.yml
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── README.md
└── .gitignore
```

---

# 🚀 Features

* Flask REST API
* PostgreSQL database
* SQLAlchemy ORM
* Dockerized application
* Kubernetes deployment
* Automated CI/CD pipeline
* Docker Hub integration
* Cloud deployment
* Automated testing
* Production-ready project structure

---

# 📡 API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| GET    | `/`           | Health check       |
| GET    | `/users`      | Retrieve all users |
| GET    | `/users/<id>` | Retrieve a user    |
| POST   | `/users`      | Create a user      |
| PUT    | `/users/<id>` | Update a user      |

---

# 🧪 Running Locally

Clone the repository:

```bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
```

Install dependencies:

```bash
pip install -r app/backend/requirements.txt
```

Run the application:

```bash
python app/backend/app.py
```

---

# 🐳 Docker

Build the image:

```bash
docker build -t alibras257/flask-backend:latest app/backend
```

Run the container:

```bash
docker run -p 5000:5000 alibras257/flask-backend:latest
```

---

# ☸️ Kubernetes

Deploy the application:

```bash
kubectl apply -f kubernetes/
```

Verify deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Access locally:

```bash
http://localhost:30910
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically performs:

* Checkout repository
* Install dependencies
* Start PostgreSQL service
* Execute Pytest
* Build Docker image
* Push Docker image to Docker Hub

---

# ✅ Testing

Execute tests locally:

```bash
pytest app/backend/tests -v
```

---

# 📦 Docker Hub

Docker image:

```
alibras257/flask-backend:latest
```

---

# 📈 Future Improvements

* Terraform infrastructure provisioning
* AWS deployment (EKS/ECS)
* Helm charts
* Argo CD GitOps
* Prometheus monitoring
* Grafana dashboards
* NGINX reverse proxy
* Redis caching
* Load balancing
* SonarCloud code quality

---

# 👨‍💻 Author

**Ibraheem Aloyinlapa**

GitHub

https://github.com/Alibras257

LinkedIn

https://www.linkedin.com/in/ibraheem-aloyinlapa-00153bb7/

---

# ⭐ Acknowledgements

This project was built to demonstrate practical DevOps engineering skills, including application development, containerization, orchestration, cloud deployment, and CI/CD automation using modern DevOps tooling.
