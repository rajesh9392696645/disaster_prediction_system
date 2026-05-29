# routes/auth_routes.py

from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_routes = Blueprint(
    "auth_routes",
    __name__
)


@auth_routes.route(
    "/register",
    methods=["POST"]
)
def register():

    try:

        data = request.get_json()

        result = AuthService.register_user(data)

        return jsonify(result), 201

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500


@auth_routes.route(
    "/login",
    methods=["POST"]
)
def login():

    try:

        data = request.get_json()

        result = AuthService.login_user(

            data["email"],
            data["password"]
        )

        return jsonify(result), 200

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500