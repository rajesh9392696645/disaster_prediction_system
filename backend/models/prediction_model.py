# models/prediction_model.py

from datetime import datetime


class PredictionModel:

    def __init__(
        self,
        disaster_type,
        prediction_accuracy,
        risk_level,
        location,
        predicted_time,
        satellite_image=None
    ):

        self.disaster_type = disaster_type
        self.prediction_accuracy = prediction_accuracy
        self.risk_level = risk_level
        self.location = location
        self.predicted_time = predicted_time
        self.satellite_image = satellite_image

        self.created_at = datetime.utcnow()

    def to_dict(self):

        return {

            "disaster_type": self.disaster_type,
            "prediction_accuracy": self.prediction_accuracy,
            "risk_level": self.risk_level,
            "location": self.location,
            "predicted_time": self.predicted_time,
            "satellite_image": self.satellite_image,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):

        return {

            "id": str(data.get("_id")),
            "disaster_type": data.get("disaster_type"),
            "prediction_accuracy": data.get("prediction_accuracy"),
            "risk_level": data.get("risk_level"),
            "location": data.get("location"),
            "predicted_time": data.get("predicted_time"),
            "satellite_image": data.get("satellite_image"),
            "created_at": data.get("created_at")
        }