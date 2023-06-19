from flask import Blueprint


api_v1_blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_blueprint.after_request
def set_response_after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Content-Type"] = "application/json"
    return response
