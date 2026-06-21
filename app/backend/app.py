import os
import time
from flask import Flask, request, jsonify
from sqlalchemy.exc import OperationalError, IntegrityError

from extensions import db
from models import User


def create_app():
    app = Flask(__name__)

    # DB config
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://devuser:devpass@postgres:5432/devdb"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # init db
    db.init_app(app)

    # create tables with retry (for Kubernetes/Postgres startup delay)
    with app.app_context():
        for i in range(10):
            try:
                db.create_all()
                print("Database connected successfully")
                break
            except OperationalError:
                print(f"DB not ready, retrying... ({i+1}/10)")
                time.sleep(2)

    # ---------------- ROUTES ---------------- #

    @app.route("/")
    def home():
        return jsonify({"status": "connected to app layer"})

    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON body provided"}), 400

        if "name" not in data or "email" not in data:
            return jsonify({"error": "Name and email are required"}), 400

        user = User(name=data["name"], email=data["email"])

        try:
            db.session.add(user)
            db.session.commit()

            return jsonify({
                "message": "User created successfully",
                "user": user.to_dict()
            }), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Email already exists"}), 409

    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()
        return jsonify({
            "count": len(users),
            "users": [u.to_dict() for u in users]
        })

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_dict())

    @app.route("/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()

        if "name" in data:
            user.name = data["name"]

        if "email" in data:
            user.email = data["email"]

        try:
            db.session.commit()
            return jsonify({
                "message": "User updated successfully",
                "user": user.to_dict()
            })
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Email already exists"}), 409

    return app


# Gunicorn entrypoint
app = create_app()