# models/alert_model.py

from datetime import datetime


class AlertModel:

    def __init__(
        self,
        alert_title,
        disaster_type,
        alert_message,
        alert_level,
        location,
        status="active"
    ):

        self.alert_title = alert_title
        self.disaster_type = disaster_type
        self.alert_message = alert_message
        self.alert_level = alert_level
        self.location = location
        self.status = status

        self.created_at = datetime.utcnow()

    def to_dict(self):

        return {

            "alert_title": self.alert_title,
            "disaster_type": self.disaster_type,
            "alert_message": self.alert_message,
            "alert_level": self.alert_level,
            "location": self.location,
            "status": self.status,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):

        return {

            "id": str(data.get("_id")),
            "alert_title": data.get("alert_title"),
            "disaster_type": data.get("disaster_type"),
            "alert_message": data.get("alert_message"),
            "alert_level": data.get("alert_level"),
            "location": data.get("location"),
            "status": data.get("status"),
            "created_at": data.get("created_at")
        }