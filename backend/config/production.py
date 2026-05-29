# config/production.py

class ProductionConfig:

    DEBUG = False

    TESTING = False

    SECRET_KEY = "production_secret_key"

    MONGO_URI = "mongodb://localhost:27017/ai_disaster_prediction_db"

    ENV = "production"

    API_TITLE = "AI Disaster Prediction API - Production"

    API_VERSION = "1.0"

    JWT_SECRET_KEY = "jwt_prod_secret"

    UPLOAD_FOLDER = "uploads/"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024