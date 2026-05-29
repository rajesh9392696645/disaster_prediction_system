# routes/gis_routes.py

from flask import Blueprint, jsonify
from services.gis_service import GISService

gis_routes = Blueprint(
    "gis_routes",
    __name__
)


@gis_routes.route(
    "/generate-map/<float:latitude>/<float:longitude>/<disaster>",
    methods=["GET"]
)
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