# database/__init__.py

from .mongo import (
    mongo_database,
    db,
    users_collection,
    prediction_collection,
    alerts_collection,
    disaster_collection
)

__all__ = [

    "mongo_database",

    "db",

    "users_collection",

    "prediction_collection",

    "alerts_collection",

    "disaster_collection"
]