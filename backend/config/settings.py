# config/settings.py

import os

class BaseConfig:

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/ai_disaster_prediction_db"
    )

    DEBUG = False

    TESTING = False

    API_TITLE = "AI Disaster Prediction System"

    API_VERSION = "1.0"

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "jwt_secret_key"
    )

    UPLOAD_FOLDER = "uploads/"

    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "csv"
    }

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class DevelopmentConfig(BaseConfig):

    DEBUG = True

    ENV = "development"


class ProductionConfig(BaseConfig):

    DEBUG = False

    ENV = "production"


class TestingConfig(BaseConfig):

    TESTING = True

    DEBUG = True

    ENV = "testing"