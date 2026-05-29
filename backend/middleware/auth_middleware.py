# middleware/auth_middleware.py

from functools import wraps
from flask import request, jsonify
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "jwt_secret_key"
)


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        # Get token from headers
        if "Authorization" in request.headers:

            auth_header = request.headers[
                "Authorization"
            ]

            try:

                token = auth_header.split(" ")[1]

            except:

                return jsonify({

                    "success": False,

                    "message":
                    "Invalid Token Format"

                }), 401

        # Token missing
        if not token:

            return jsonify({

                "success": False,

                "message":
                "Token is Missing"

            }), 401

        try:

            # Decode JWT token
            data = jwt.decode(

                token,

                SECRET_KEY,

                algorithms=["HS256"]
            )

            current_user = {

                "user_id":
                data.get("user_id"),

                "email":
                data.get("email"),

                "role":
                data.get("role")
            }

        except jwt.ExpiredSignatureError:

            return jsonify({

                "success": False,

                "message":
                "Token Expired"

            }), 401

        except jwt.InvalidTokenError:

            return jsonify({

                "success": False,

                "message":
                "Invalid Token"

            }), 401

        return f(
            current_user,
            *args,
            **kwargs
        )

    return decorated