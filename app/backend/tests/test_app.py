from app import create_app


def test_home():
    app = create_app()
    app.testing = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "connected to app layer",
        "service": "devops-production-platform",
    }


def test_health():
    app = create_app()
    app.testing = True
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy",
        "service": "flask-backend",
    }