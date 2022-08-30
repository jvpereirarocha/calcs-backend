from flask import Flask

from calculations.adapters.orms.mappers import start_mappers

def create_app(config_name: str):
    app = Flask(__name__)
    start_mappers()
    return app