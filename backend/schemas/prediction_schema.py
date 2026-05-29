# schemas/prediction_schema.py

from marshmallow import Schema, fields, validate


class PredictionSchema(Schema):

    disaster_type = fields.Str(
        required=True,
        validate=validate.OneOf([
            "flood",
            "wildfire",
            "cyclone",
            "earthquake",
            "landslide",
            "drought"
        ])
    )

    prediction_accuracy = fields.Float(
        required=True,
        validate=validate.Range(
            min=0,
            max=100
        )
    )

    risk_level = fields.Str(
        required=True,
        validate=validate.OneOf([
            "LOW",
            "MEDIUM",
            "HIGH"
        ])
    )

    location = fields.Str(
        required=True
    )

    predicted_time = fields.DateTime(
        required=True
    )

    satellite_image = fields.Str(
        required=False
    )

    created_at = fields.DateTime(
        dump_only=True
    )