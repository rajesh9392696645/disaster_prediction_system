# schemas/user_schema.py

from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    full_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=3,
            max=100
        )
    )

    email = fields.Email(
        required=True
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(
            min=8
        )
    )

    role = fields.Str(
        validate=validate.OneOf([
            "admin",
            "user",
            "rescue_team"
        ]),
        missing="user"
    )

    phone = fields.Str(
        required=False,
        validate=validate.Length(
            min=10,
            max=15
        )
    )

    location = fields.Str(
        required=False
    )

    created_at = fields.DateTime(
        dump_only=True
    )