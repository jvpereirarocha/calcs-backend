from enum import Enum
from os import getenv


class BaseConfig:
    IS_TESTING = False
    FLASK_ENV = getenv("FLASK_ENV")
    DATABASE_URI = getenv("DATABASE_URI")


class DevelopmentConfig(BaseConfig):
    IS_TESTING = False


class ProductionConfig(BaseConfig):
    IS_TESTING = False


class TestingConfig(BaseConfig):
    IS_TESTING = True
    DATABASE_URI = "sqlite:///app-test.db"


environments = {
    "production": ProductionConfig(),
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
}
