# schemas/alert_schema.py

from marshmallow import Schema, fields, validate


class AlertSchema(Schema):

    alert_title = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=100)
    )

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

    alert_message = fields.Str(
        required=True,
        validate=validate.Length(min=10)
    )

    alert_level = fields.Str(
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

    status = fields.Str(
        missing="active"
    )

    created_at = fields.DateTime(
        dump_only=True
    )