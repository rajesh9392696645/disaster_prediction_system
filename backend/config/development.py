# config/development.py

class DevelopmentConfig:

    DEBUG = True

    TESTING = False

    SECRET_KEY = "development_secret_key"

    MONGO_URI = "mongodb://localhost:27017/ai_disaster_prediction_db"

    ENV = "development"

    API_TITLE = "AI Disaster Prediction API - Development"

    API_VERSION = "1.0"

    JWT_SECRET_KEY = "jwt_dev_secret"

    UPLOAD_FOLDER = "uploads/"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024