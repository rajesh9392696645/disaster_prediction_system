# controllers/satellite_controller.py

from flask import jsonify
from services.satellite_service import (
    SatelliteService
)

satellite_service = SatelliteService()


class SatelliteController:

    @staticmethod
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