# DevOps Production Platform

A full-stack DevOps project demonstrating a containerised Flask backend with PostgreSQL, deployed using Docker and Kubernetes.

This project focuses on real-world DevOps practices including containerisation, orchestration, deployment debugging, and production-style configuration.

---

## 🚀 Live API

Kubernetes NodePort:

http://localhost:30910/


Response:
```json
{
  "status": "connected to app layer"
}
🧠 Architecture

Client → Flask API (Gunicorn) → PostgreSQL → Docker → Kubernetes

⚙️ Tech Stack
Python 3.12
Flask
SQLAlchemy
PostgreSQL
Docker
Kubernetes
Gunicorn
Pytest
GitHub
📁 Project Structure
devops-production-platform/
│
├── app/
│   ├── backend/
│   │   ├── app.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── config.py
│   │   ├── utils.py
│   │   ├── requirements.txt
│   │   └── tests/
│   │       └── test_app.py
│
├── docker/
├── kubernetes/
├── scripts/
├── monitoring/
├── terraform/
└── README.md
🔧 Setup Instructions
1. Clone repository
git clone https://github.com/Alibras257/devops-production-platform.git
cd devops-production-platform
2. Run with Docker
docker build -t flask-backend .
docker run -p 5000:5000 flask-backend
3. Deploy to Kubernetes
kubectl apply -f kubernetes/
kubectl get pods
kubectl get svc
4. Test API
curl http://localhost:30910/
🗄️ Environment Variables

The application uses:

DATABASE_URL=postgresql://user:password@host:5432/dbname

⚠️ IMPORTANT:

Must NOT use https://
Must be a valid PostgreSQL connection string
🧪 Run Tests
pytest app/backend/tests -v
🐳 Docker
Multi-stage containerised Flask app
Runs using Gunicorn
Optimised lightweight Python image
☸️ Kubernetes
Deployment: Flask backend
Service: NodePort
Exposes container port 5000 → 30910
🧯 Common Issues
CrashLoopBackOff

Usually caused by:

Wrong DATABASE_URL
Missing dependencies
Import errors
SQLAlchemy Error
Can't load plugin: sqlalchemy.dialects:https

Fix:
Use:

postgresql://

NOT:

https://
📌 Key Achievements
Fixed circular import issues in Flask app
Resolved SQLAlchemy database connection problems
Built Docker container successfully
Deployed to Kubernetes cluster
Debugged CrashLoopBackOff issues
Exposed working NodePort service
End-to-end API validation completed
👨‍💻 Author

DevOps Project – Ibraheem Aloyinlapa

📊 Status

✔ Backend working
✔ Kubernetes deployed
✔ Database connected
✔ API fully functional