import os

class Config:
    APP_NAME = "DevOps Production Platform"
    VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("FLASK_ENV", "development")
