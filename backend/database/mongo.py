# database/mongo.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

class MongoDatabase:

    def __init__(self):

        self.mongo_uri = os.getenv(
            "MONGO_URI",
            "mongodb://localhost:27017/"
        )

        self.database_name = os.getenv(
            "DATABASE_NAME",
            "ai_disaster_prediction_db"
        )

        self.client = None
        self.db = None

    def connect(self):

        try:

            self.client = MongoClient(
                self.mongo_uri
            )

            self.db = self.client[
                self.database_name
            ]

            print(
                "MongoDB Connected Successfully"
            )

            return self.db

        except Exception as e:

            print(
                f"MongoDB Connection Error: {e}"
            )

            return None

    def get_collection(self, collection_name):

        if self.db is None:

            self.connect()

        return self.db[collection_name]

    def close_connection(self):

        if self.client:

            self.client.close()

            print(
                "MongoDB Connection Closed"
            )


# Initialize Database Object
mongo_database = MongoDatabase()

# Connect Database
db = mongo_database.connect()

# Collections
users_collection = db["users"]

prediction_collection = db["predictions"]

alerts_collection = db["alerts"]

disaster_collection = db["disasters"]