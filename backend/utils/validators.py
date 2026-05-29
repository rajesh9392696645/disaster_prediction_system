# utils/validators.py

import re


class Validators:

    @staticmethod
    def validate_email(email):

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        return re.match(pattern, email)

    @staticmethod
    def validate_password(password):

        """
        Password Rules:
        - Minimum 8 characters
        - At least 1 uppercase
        - At least 1 lowercase
        - At least 1 number
        """

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

        return re.match(pattern, password)

    @staticmethod
    def validate_phone(phone):

        pattern = r'^[6-9]\d{9}$'

        return re.match(pattern, phone)

    @staticmethod
    def validate_coordinates(
        latitude,
        longitude
    ):

        if latitude < -90 or latitude > 90:

            return False

        if longitude < -180 or longitude > 180:

            return False

        return True

    @staticmethod
    def validate_disaster_type(
        disaster_type
    ):

        valid_types = [

            "flood",
            "wildfire",
            "cyclone",
            "earthquake",
            "landslide",
            "drought"
        ]

        return disaster_type.lower() in valid_types

    @staticmethod
    def validate_risk_level(
        risk_level
    ):

        valid_levels = [

            "LOW",
            "MEDIUM",
            "HIGH"
        ]

        return risk_level.upper() in valid_levels

    @staticmethod
    def validate_required_fields(
        data,
        required_fields
    ):

        missing_fields = []

        for field in required_fields:

            if field not in data or data[field] == "":

                missing_fields.append(field)

        return missing_fields