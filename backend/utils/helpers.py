# utils/helpers.py

import os
import uuid
from datetime import datetime


def generate_unique_id():

    return str(uuid.uuid4())


def current_timestamp():

    return datetime.utcnow()


def allowed_file(filename, allowed_extensions):

    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions


def format_response(
    success=True,
    message="",
    data=None,
    status_code=200
):

    return {

        "success": success,
        "message": message,
        "data": data,
        "status_code": status_code
    }


def create_upload_folder(folder_path):

    if not os.path.exists(folder_path):

        os.makedirs(folder_path)

        return True

    return False


def convert_objectid_to_str(data):

    if isinstance(data, list):

        for item in data:

            if "_id" in item:

                item["_id"] = str(item["_id"])

    elif isinstance(data, dict):

        if "_id" in data:

            data["_id"] = str(data["_id"])

    return data


def calculate_risk_level(probability):

    if probability >= 0.8:

        return "HIGH"

    elif probability >= 0.5:

        return "MEDIUM"

    else:

        return "LOW"