import os
import time

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError, IntegrityError

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://devuser:devpass@postgres:5432/devdb"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import models after initializing db
    from models import User

    # Wait for PostgreSQL to become available
    with app.app_context():
        retries = 10

        for i in range(retries):
            try:
                db.create_all()
                print("Database connected successfully")
                break
            except OperationalError:
                print(f"DB not ready, retrying... ({i + 1}/{retries})")
                time.sleep(2)

    @app.route("/")
    def home():
        return jsonify({
            "status": "connected to app layer"
        })

    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()

        # Basic validation
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        if "name" not in data or "email" not in data:
            return jsonify({"error": "Both name and email are required"}), 400

        user = User(
            name=data["name"],
            email=data["email"]
        )

        try:
            db.session.add(user)
            db.session.commit()

            return jsonify(user.to_dict()), 201

        except IntegrityError:
            db.session.rollback()

            return jsonify({
                "error": "Email already exists."
            }), 409

    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()

        return jsonify([user.to_dict() for user in users]), 200

    return app
