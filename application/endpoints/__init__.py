from .blueprint import api_v1_blueprint
from .profile_api import profile_blueprint


api_v1_blueprint.register_blueprint(profile_blueprint)

