import os
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def create_app():
    from models import User
    print(db.metadata.tables)
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://devuser:devpass@postgres:5432/devdb"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # ✅ THIS is where your retry logic goes
    with app.app_context():
        retries = 10

        for i in range(retries):
            try:
                db.create_all()
                print("Database connected successfully")
                break
            except OperationalError:
                print(f"DB not ready, retrying... ({i+1}/{retries})")
                time.sleep(2)

    @app.route("/")
    def home():
        return {"status": "connected to app layer"}

    return app
