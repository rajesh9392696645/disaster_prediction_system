# services/alert_service.py

from database.mongo import alerts_collection
from models.alert_model import AlertModel
from utils.helpers import current_timestamp


class AlertService:

    @staticmethod
    def create_alert(data):

        alert = AlertModel(
            alert_title=data["alert_title"],
            disaster_type=data["disaster_type"],
            alert_message=data["alert_message"],
            alert_level=data["alert_level"],
            location=data["location"]
        )

        result = alerts_collection.insert_one(
            alert.to_dict()
        )

        return {

            "message": "Alert Created Successfully",
            "alert_id": str(result.inserted_id)
        }

    @staticmethod
    def get_all_alerts():

        alerts = list(
            alerts_collection.find()
        )

        for alert in alerts:

            alert["_id"] = str(alert["_id"])

        return alerts

    @staticmethod
    def delete_alert(alert_id):

        result = alerts_collection.delete_one(
            {"_id": alert_id}
        )

        return result.deleted_count