from flask import Blueprint, jsonify, request

from application.ports.user import CreateUserInputPort
from application.services.user_service import CreateUserService
from infrastructure.database.repository.users.user_repo import UserRepo
from libs.types.identifiers import UserUUID


user_blueprint = Blueprint(__name__, url_prefix="/users")


@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    pass

@user_blueprint.route("/new", methods=["POST"])
def create_user():
    
    data = request.data
    user_requester = CreateUserInputPort(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        avatar=data.get("avatar", None)
    )

    repo = UserRepo()
    service = CreateUserService(requester=user_requester, repo=repo)
    service.operation()

    return jsonify({"User is created!"}), 201
