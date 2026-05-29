# config/database.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["ai_disaster_prediction_db"]

users_collection = db["users"]
prediction_collection = db["predictions"]
alerts_collection = db["alerts"]
disaster_collection = db["disasters"]