# DevOps Production Platform 🚀

A full-stack DevOps project demonstrating a **containerized Flask API**, **PostgreSQL database**, **CI/CD pipeline**, and **cloud deployment on Render**.

---

## 🌐 Live Application

👉 https://devops-production-platform.onrender.com

---

## 📌 Features

- Flask REST API (CRUD operations)
- PostgreSQL database (cloud-hosted on Render)
- Docker containerization
- Gunicorn production server
- GitHub Actions CI pipeline
- Automatic deployment on Render (CD)
- Circular import-safe architecture (production pattern)

---

## 🧱 Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- PostgreSQL (Render)
- Docker
- Gunicorn
- GitHub Actions
- Render (Cloud Hosting)

---

## 📡 API Endpoints

### Health Check

GET /
GET /users
POST /users
GET /users/<id>
PUT /users/<id>
DELETE /users/<id>
### Users API


---

## 🧪 Example Requests

### Create User
```bash
curl -X POST https://devops-production-platform.onrender.com/users \
-H "Content-Type: application/json" \
-d '{"name":"Ali","email":"ali@example.com"}'

### Get All Users
curl https://devops-production-platform.onrender.com/users

## Update User
curl -X PUT https://devops-production-platform.onrender.com/users/1 \
-H "Content-Type: application/json" \
-d '{"name":"Updated Name","email":"updated@example.com"}'

## Delete User
curl -X DELETE https://devops-production-platform.onrender.com/users/1

## Run locally (Docker)
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform

docker compose up --build

## App run at 
http://localhost:5000

## Environment Variables

## Create a .env file or set in Render:
DATABASE_URL=your_postgres_connection_string
FLASK_ENV=production


🏗 Architecture Overview

This project follows a production-grade DevOps workflow:

Flask application containerized using Docker
PostgreSQL database hosted on Render
Gunicorn used as production WSGI server
GitHub Actions used for CI (tests & validation)
Render handles continuous deployment (CD)
Factory pattern used to prevent circular imports

🔄 CI/CD Pipeline

Continuous Integration (GitHub Actions)
Runs tests using pytest
Validates Python environment
Ensures build stability before deployment

Continuous Deployment (Render)

Automatically deploys from main branch
Builds Docker image
Restarts service on new commits

## Project Structure
app/
 └── backend/
     ├── app.py
     ├── models.py
     ├── routes.py
     ├── config.py
     ├── requirements.txt
     └── tests/

     🚀 Key DevOps Concepts Demonstrated
Containerization (Docker)
Cloud deployment (Render)
CI/CD pipeline (GitHub Actions + Render)
Infrastructure as Code mindset
Environment-based configuration
Microservice-style backend structure
Production debugging (imports, DB, deployment issues)

👨‍💻 Author

Ibraheem Aloyinlapa

📌 Future Improvements
Add database migrations (Alembic)
Add authentication (JWT)
Add monitoring (Prometheus + Grafana)
Deploy with Kubernetes (EKS / GKE)
Add frontend dashboard