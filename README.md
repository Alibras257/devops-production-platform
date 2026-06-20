# DevOps Production Platform

A production-ready backend application built with **Flask**, **PostgreSQL**, and **Docker**. This project demonstrates modern DevOps practices, containerization, database integration, and backend API development.

---

## Features

* Flask REST API
* PostgreSQL database
* SQLAlchemy ORM
* Dockerized backend and database
* Docker Compose orchestration
* Automatic database initialization
* Production-ready project structure

---

## Tech Stack

* Python 3.12
* Flask
* SQLAlchemy
* PostgreSQL 16
* Docker
* Docker Compose
* Gunicorn

---

## Project Structure

```text
devops-production-platform/
│
├── app/
│   └── backend/
│       ├── app.py
│       ├── models.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
```

### Build and start the application

```bash
docker compose up --build
```

The application will be available at:

```
http://localhost:5000
```

---

## Database

The application uses PostgreSQL running inside Docker.

Default configuration:

| Variable | Value    |
| -------- | -------- |
| Database | devdb    |
| Username | devuser  |
| Password | devpass  |
| Host     | postgres |
| Port     | 5432     |

SQLAlchemy automatically creates the required tables during application startup.

---

## Current API

### Health Check

```
GET /
```

Example response:

```json
{
    "status": "connected to app layer"
}
```

---

## Docker Commands

Build containers

```bash
docker compose up --build
```

Run in detached mode

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

Remove containers and database volume

```bash
docker compose down -v
```

View logs

```bash
docker compose logs -f
```

---

## Future Improvements

* CRUD API endpoints
* Flask-Migrate database migrations
* JWT Authentication
* Unit and integration tests
* GitHub Actions CI/CD
* Docker image publishing
* Kubernetes deployment
* Monitoring with Prometheus and Grafana
* Nginx reverse proxy

---

## Learning Goals

This project is designed to demonstrate:

* Backend API development
* Docker containerization
* PostgreSQL integration
* SQLAlchemy ORM
* DevOps best practices
* Production-ready application architecture

---

## Author

**Ibraheem Aloyinlapa**

GitHub: https://github.com/Alibras257

