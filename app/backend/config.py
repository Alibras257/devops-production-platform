import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://devuser:devpass@localhost:5432/devdb",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False