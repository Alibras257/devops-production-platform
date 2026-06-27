from flask import jsonify


def register_routes(app):
    @app.route("/")
    def home():
        return jsonify(
            {
                "status": "connected to app layer",
                "service": "devops-production-platform",
            }
        )

    @app.route("/health")
    def health():
        return jsonify(
            {
                "status": "healthy",
                "service": "flask-backend",
            }
        )

    @app.route("/api/info")
    def info():
        return jsonify(
            {
                "application": "devops-production-platform",
                "environment": app.config.get("FLASK_ENV", "production"),
                "status": "running",
            }
        )