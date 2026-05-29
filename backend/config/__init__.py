# config/__init__.py

from .database import *
from .development import DevelopmentConfig
from .production import ProductionConfig
from .settings import (
    BaseConfig,
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig
)

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}