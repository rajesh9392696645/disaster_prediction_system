# routes/alert_routes.py

from flask import Blueprint, request, jsonify
from services.alert_service import AlertService

alert_routes = Blueprint(
    "alert_routes",
    __name__
)


@alert_routes.route(
    "/create-alert",
    methods=["POST"]
)
def create_alert():

    try:

        data = request.get_json()

        result = AlertService.create_alert(data)

        return jsonify(result), 201

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500


@alert_routes.route(
    "/all-alerts",
    methods=["GET"]
)
def get_all_alerts():

    try:

        alerts = AlertService.get_all_alerts()

        return jsonify({

            "success": True,
            "data": alerts

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500