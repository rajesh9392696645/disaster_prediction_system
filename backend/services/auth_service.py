# services/auth_service.py

from database.mongo import users_collection
from models.user_model import UserModel
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class AuthService:

    @staticmethod
    def register_user(data):

        existing_user = users_collection.find_one({
            "email": data["email"]
        })

        if existing_user:

            return {
                "success": False,
                "message": "Email already exists"
            }

        hashed_password = generate_password_hash(
            data["password"]
        )

        user = UserModel(
            full_name=data["full_name"],
            email=data["email"],
            password=hashed_password,
            phone=data.get("phone"),
            location=data.get("location")
        )

        result = users_collection.insert_one(
            user.to_dict()
        )

        return {

            "success": True,
            "user_id": str(result.inserted_id)
        }

    @staticmethod
    def login_user(email, password):

        user = users_collection.find_one({
            "email": email
        })

        if not user:

            return {
                "success": False,
                "message": "User not found"
            }

        if check_password_hash(
            user["password"],
            password
        ):

            user["_id"] = str(user["_id"])

            return {

                "success": True,
                "user": user
            }

        return {

            "success": False,
            "message": "Invalid Password"
        }