from .blueprint import api_v1_blueprint
from .user_api import user_blueprint


api_v1_blueprint.register_blueprint(user_blueprint)

