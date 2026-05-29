# routes/satellite_routes.py

from flask import Blueprint, jsonify
from services.satellite_service import (
    SatelliteService
)

satellite_routes = Blueprint(
    "satellite_routes",
    __name__
)

satellite_service = SatelliteService()


@satellite_routes.route(
    "/satellite-data",
    methods=["GET"]
)
def get_satellite_data():

    try:

        data = satellite_service.fetch_satellite_data()

        return jsonify({

            "success": True,

            "data": data

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500