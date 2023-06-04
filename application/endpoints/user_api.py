from flask import Blueprint, request
from application.parsers.user import AllUsersParser, CreatedOrUpdatedUserParser, GetOneUserParser

from application.ports.user import CreateUser
from application.services.user_service import CreateUserService, FetchOneUserService, GetUsersService
from infrastructure.database.repository.users.user_repo import UserRepo
from libs.types.identifiers import UserUUID


user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    service = GetUsersService(repo=UserRepo())
    users = service.get_all()
    parser = AllUsersParser()
    return parser.to_json(data=users), 200

@user_blueprint.route("/new", methods=["POST"])
def create_user_and_person():
    data = request.get_json()
    user_requester = CreateUser(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        avatar=data.get("avatar", None)
    )
    repo = UserRepo()
    service = CreateUserService(requester=user_requester, repo=repo)
    service.create_or_update()
    parser = CreatedOrUpdatedUserParser()
    return parser.to_json(), 201

@user_blueprint.route("/get_first_user", methods=["GET"])
def retrieve_the_first_user():
    repo = UserRepo()
    service = FetchOneUserService(repo=repo)
    first_user = service.get_first_user()
    parser = GetOneUserParser()
    return parser.to_json(data=first_user), 200
