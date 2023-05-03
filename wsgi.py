from flask import Flask

from infrastructure.config.configuration_objects import environments
from infrastructure.database.orms.mappers import start_mappers
from application.endpoints import api_v1_blueprint

def create_app(config_name: str):
    app = Flask(__name__)
    current_configuration = environments.get(config_name)
    app.config.from_object(current_configuration)
    app.register_blueprint(api_v1_blueprint)
    start_mappers()
    return app