# models/disaster_model.py

from datetime import datetime


class DisasterModel:

    def __init__(
        self,
        disaster_name,
        disaster_type,
        severity,
        affected_area,
        latitude,
        longitude,
        weather_condition,
        status="detected"
    ):

        self.disaster_name = disaster_name
        self.disaster_type = disaster_type
        self.severity = severity
        self.affected_area = affected_area

        self.latitude = latitude
        self.longitude = longitude

        self.weather_condition = weather_condition

        self.status = status

        self.created_at = datetime.utcnow()

    def to_dict(self):

        return {

            "disaster_name": self.disaster_name,
            "disaster_type": self.disaster_type,
            "severity": self.severity,
            "affected_area": self.affected_area,

            "latitude": self.latitude,
            "longitude": self.longitude,

            "weather_condition": self.weather_condition,

            "status": self.status,

            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):

        return {

            "id": str(data.get("_id")),

            "disaster_name": data.get("disaster_name"),

            "disaster_type": data.get("disaster_type"),

            "severity": data.get("severity"),

            "affected_area": data.get("affected_area"),

            "latitude": data.get("latitude"),

            "longitude": data.get("longitude"),

            "weather_condition": data.get("weather_condition"),

            "status": data.get("status"),

            "created_at": data.get("created_at")
        }