from flask import Blueprint, jsonify, request
from application.requests.person import CreatePerson

from application.requests.user import CreateUser, LoginRequest
from application.responses.login_response import LoginResponse
from application.responses.user_and_person_created import UserAndPersonCreated
from application.services.person_service import CreatePersonService
from application.services.token_required_service import token_required
from application.services.user_service import CreateUserService, LoginService
from infrastructure.database.repository.profiles.profile_repo import ProfileRepo
from libs.types.identifiers import PersonUUID, UserUUID


profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")


@profile_blueprint.route("/register", methods=["POST"])
def register_new_profile():
    data = request.get_json()
    # First of all, creating a user
    user_requester = CreateUser(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        confirm_password=data["confirmPassword"],
        avatar=data.get("avatar", None),
    )

    user_requester.validate_request()

    profile_repo = ProfileRepo()
    user_service = CreateUserService(requester=user_requester, repo=profile_repo)
    user_request = user_service.create_or_update()
    if user_request.error:
        return jsonify({"error": "The user already exists"}), 400
    user = user_request.user
    # After that, creating a person instance
    person_requester = CreatePerson(
        person_id=PersonUUID(),
        first_name=data["firstName"],
        last_name=data["lastName"],
        date_of_birth=data["dateOfBirth"],
        user_id=user.user_id,
    )
    person_requester.validate_request()

    person_service = CreatePersonService(requester=person_requester, repo=profile_repo)
    person = person_service.create_or_update()

    profile_repo.commit()

    output = UserAndPersonCreated(user=user, person=person)
    response, status_code = output.to_json()
    return response, status_code


@profile_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    profile_repo = ProfileRepo()
    login_requester = LoginRequest(email=data["email"], password=data["password"])
    login_requester.validate_request()
    login_service: LoginService = LoginService(
        requester=login_requester, repo=profile_repo, error=""
    )
    token = login_service.make_login()
    error = ""
    if login_service.error:
        error = login_service.error
    response = LoginResponse(email=data["email"], token=token, error=error)
    message, status_code = response.to_json()
    return message, status_code


@profile_blueprint.route("/me", methods=["GET"])
@token_required
def get_my_profile(user_info):
    profile_repo = ProfileRepo()
    user = profile_repo.get_first_user_by_id(user_id=UserUUID(user_info["user_id"]))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "Token validado com sucesso!!"}), 200
