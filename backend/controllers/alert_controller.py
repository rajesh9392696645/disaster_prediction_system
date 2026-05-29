# controllers/alert_controller.py

from flask import request, jsonify
from services.alert_service import AlertService
from schemas.alert_schema import AlertSchema

alert_schema = AlertSchema()


class AlertController:

    @staticmethod
    def create_alert():

        try:

            data = request.get_json()

            errors = alert_schema.validate(data)

            if errors:

                return jsonify({

                    "success": False,

                    "errors": errors

                }), 400

            result = AlertService.create_alert(data)

            return jsonify({

                "success": True,

                "data": result

            }), 201

        except Exception as e:

            return jsonify({

                "success": False,

                "message": str(e)

            }), 500

    @staticmethod
    def get_alerts():

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