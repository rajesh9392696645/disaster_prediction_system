# routes/report_routes.py

from flask import Blueprint, jsonify
from database.mongo import (
    prediction_collection,
    alerts_collection,
    disaster_collection
)

report_routes = Blueprint(
    "report_routes",
    __name__
)


@report_routes.route(
    "/system-report",
    methods=["GET"]
)
def system_report():

    try:

        total_predictions = prediction_collection.count_documents({})

        total_alerts = alerts_collection.count_documents({})

        total_disasters = disaster_collection.count_documents({})

        report = {

            "total_predictions":
            total_predictions,

            "total_alerts":
            total_alerts,

            "total_disasters":
            total_disasters
        }

        return jsonify({

            "success": True,

            "report": report

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500