from .blueprint import api_v1_blueprint
from .profile_api import profile_blueprint
from .expenses_api import expenses_blueprint


api_v1_blueprint.register_blueprint(profile_blueprint)
api_v1_blueprint.register_blueprint(expenses_blueprint)
