from flask import jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return {
            "message": "Welcome to the DevOps Production Platform!"
        }

    @app.route("/health")
    def health():
        return {
            "status": "healthy"
        }

    @app.route("/api/info")
    def info():
        return jsonify({
            "application": app.config["APP_NAME"],
            "version": app.config["VERSION"],
            "environment": app.config["ENVIRONMENT"],
            "status": "running"
        })
