import os
import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError, IntegrityError

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # DB config
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://devuser:devpass@postgres:5432/devdb"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Import models AFTER db init
    from app.backend.models import User

    # Create tables with retry (Postgres readiness)
    with app.app_context():
        for i in range(10):
            try:
                db.create_all()
                print("Database connected successfully")
                break
            except OperationalError:
                print(f"DB not ready, retrying... ({i+1}/10)")
                time.sleep(2)

    # ---------------- ROUTES ----------------

    @app.route("/")
    def home():
        return jsonify({"status": "connected to app layer"})

    # CREATE USER
    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.get_json()

        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        if "name" not in data or "email" not in data:
            return jsonify({"error": "name and email required"}), 400

        user = User(name=data["name"], email=data["email"])

        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "email already exists"}), 409

    # GET ALL USERS
    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()
        return jsonify({
            "count": len(users),
            "users": [u.to_dict() for u in users]
        })

    # GET SINGLE USER
    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "user not found"}), 404

        return jsonify(user.to_dict())

    # ---------------- FIX: PUT UPDATE USER ----------------
    @app.route("/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "user not found"}), 404

        data = request.get_json()

        if not data:
            return jsonify({"error": "missing JSON body"}), 400

        if "name" in data:
            user.name = data["name"]

        if "email" in data:
            user.email = data["email"]

        try:
            db.session.commit()
            return jsonify({
                "message": "user updated successfully",
                "user": user.to_dict()
            })

        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "email already exists"}), 409

    # OPTIONAL: DELETE USER
    @app.route("/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "user not found"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "user deleted"})

    return app


app = create_app()