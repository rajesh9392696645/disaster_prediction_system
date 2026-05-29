# controllers/prediction_controller.py

from flask import request, jsonify
from services.cnn_service import CNNService
from services.lstm_service import LSTMService
from services.prediction_service import (
    PredictionService
)

cnn_service = CNNService()

lstm_service = LSTMService()


class PredictionController:

    @staticmethod
    def cnn_prediction():

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

    @staticmethod
    def lstm_prediction():

        try:

            data = request.get_json()

            sequence = data["sequence"]

            result = lstm_service.predict_weather_risk(
                sequence
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

    @staticmethod
    def save_prediction():

        try:

            data = request.get_json()

            result = PredictionService.save_prediction(
                data
            )

            return jsonify({

                "success": True,

                "data": result

            }), 201

        except Exception as e:

            return jsonify({

                "success": False,

                "message": str(e)

            }), 500