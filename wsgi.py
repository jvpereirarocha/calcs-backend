from flask import Flask

from infrastructure.config.configuration_objects import environments
from calculations.adapters.orms.mappers import start_mappers

def create_app(config_name: str):
    app = Flask(__name__)
    current_configuration = environments.get(config_name)
    app.config.from_object(current_configuration)
    start_mappers()
    return app