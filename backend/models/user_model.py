# models/user_model.py

from datetime import datetime
from bson import ObjectId


class UserModel:

    def __init__(
        self,
        full_name,
        email,
        password,
        role="user",
        phone=None,
        location=None
    ):

        self.full_name = full_name
        self.email = email
        self.password = password
        self.role = role
        self.phone = phone
        self.location = location

        self.created_at = datetime.utcnow()

    def to_dict(self):

        return {

            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            "role": self.role,
            "phone": self.phone,
            "location": self.location,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):

        return {

            "id": str(data.get("_id")),
            "full_name": data.get("full_name"),
            "email": data.get("email"),
            "role": data.get("role"),
            "phone": data.get("phone"),
            "location": data.get("location"),
            "created_at": data.get("created_at")
        }