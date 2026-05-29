# controllers/gis_controller.py

from flask import jsonify
from services.gis_service import GISService


class GISController:

    @staticmethod
    def generate_map(

        latitude,
        longitude,
        disaster

    ):

        try:

            map_path = GISService.generate_disaster_map(

                latitude,
                longitude,
                disaster
            )

            return jsonify({

                "success": True,

                "map_path": map_path

            }), 200

        except Exception as e:

            return jsonify({

                "success": False,

                "message": str(e)

            }), 500