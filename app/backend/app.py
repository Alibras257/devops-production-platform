import os
import time
from flask import Flask, request, jsonify
from sqlalchemy.exc import OperationalError, IntegrityError

from app.backend.models import db, User


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        for i in range(10):
            try:
                db.create_all()
                print("Database connected successfully")
                break
            except OperationalError:
                print(f"DB not ready, retrying... ({i+1}/10)")
                time.sleep(2)

    @app.route("/")
    def home():
        return jsonify({"status": "connected to app layer"})

    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()

        user = User(name=data["name"], email=data["email"])

        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Email already exists"}), 409

    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()
        return jsonify([u.to_dict() for u in users])

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

        db.session.commit()
        return jsonify(user.to_dict())

    @app.route("/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted"})

    return app


app = create_app()