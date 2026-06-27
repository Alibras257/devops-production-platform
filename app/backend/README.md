# Backend Service

This directory contains the Flask backend service for the DevOps Production Platform.

## Features

- Flask-based REST API
- PostgreSQL integration with SQLAlchemy
- Prometheus metrics endpoint
- Dockerized runtime with Gunicorn
- Health endpoint for container and Kubernetes probes

## Main Endpoints

- `/` - service status
- `/health` - health check
- `/users` - list or create users
- `/users/<id>` - retrieve or update a user
- `/metrics` - Prometheus metrics endpoint

## Local Run

```bash
pip install -r requirements.txt
python app.py
Docker Run
bash
docker build -t flask-backend .
docker run -p 5000:5000 flask-backend