# services/prediction_service.py

from database.mongo import prediction_collection
from models.prediction_model import PredictionModel


class PredictionService:

    @staticmethod
    def save_prediction(data):

        prediction = PredictionModel(

            disaster_type=data["disaster_type"],

            prediction_accuracy=data[
                "prediction_accuracy"
            ],

            risk_level=data["risk_level"],

            location=data["location"],

            predicted_time=data[
                "predicted_time"
            ],

            satellite_image=data.get(
                "satellite_image"
            )
        )

        result = prediction_collection.insert_one(
            prediction.to_dict()
        )

        return {

            "message":
            "Prediction Saved Successfully",

            "prediction_id":
            str(result.inserted_id)
        }

    @staticmethod
    def get_predictions():

        predictions = list(
            prediction_collection.find()
        )

        for prediction in predictions:

            prediction["_id"] = str(
                prediction["_id"]
            )

        return predictions