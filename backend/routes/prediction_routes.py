# routes/prediction_routes.py

from flask import Blueprint, request, jsonify
from services.prediction_service import (
    PredictionService
)
from services.cnn_service import CNNService
from services.lstm_service import (
    LSTMService
)

prediction_routes = Blueprint(
    "prediction_routes",
    __name__
)

cnn_service = CNNService()

lstm_service = LSTMService()


@prediction_routes.route(
    "/cnn-predict",
    methods=["POST"]
)
def cnn_predict():

    try:

        data = request.get_json()

        image_path = data["image_path"]

        result = cnn_service.predict_disaster(
            image_path
        )

        return jsonify({

            "success": True,

            "prediction": result

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


@prediction_routes.route(
    "/lstm-predict",
    methods=["POST"]
)
def lstm_predict():

    try:

        data = request.get_json()

        sequence_data = data["sequence"]

        result = lstm_service.predict_weather_risk(
            sequence_data
        )

        return jsonify({

            "success": True,

            "prediction": result

        }), 200

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


@prediction_routes.route(
    "/save-prediction",
    methods=["POST"]
)
def save_prediction():

    try:

        data = request.get_json()

        result = PredictionService.save_prediction(
            data
        )

        return jsonify(result), 201

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500