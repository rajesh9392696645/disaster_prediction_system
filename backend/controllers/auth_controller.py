# controllers/auth_controller.py

from flask import request, jsonify
from services.auth_service import AuthService
from schemas.user_schema import UserSchema
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "jwt_secret_key"
)

user_schema = UserSchema()


class AuthController:

    @staticmethod
    def register():

        try:

            data = request.get_json()

            errors = user_schema.validate(data)

            if errors:

                return jsonify({

                    "success": False,

                    "errors": errors

                }), 400

            result = AuthService.register_user(data)

            return jsonify(result), 201

        except Exception as e:

            return jsonify({

                "success": False,

                "message": str(e)

            }), 500

    @staticmethod
    def login():

        try:

            data = request.get_json()

            result = AuthService.login_user(

                data["email"],
                data["password"]
            )

            if result["success"]:

                token = jwt.encode({

                    "user_id":
                    result["user"]["_id"],

                    "email":
                    result["user"]["email"],

                    "role":
                    result["user"]["role"],

                    "exp":
                    datetime.utcnow() +
                    timedelta(hours=24)

                },

                SECRET_KEY,

                algorithm="HS256")

                return jsonify({

                    "success": True,

                    "token": token,

                    "user":
                    result["user"]

                }), 200

            return jsonify(result), 401

        except Exception as e:

            return jsonify({

                "success": False,

                "message": str(e)

            }), 500