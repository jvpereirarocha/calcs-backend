from flask import Blueprint, jsonify, request
from application.requests.person import CreatePerson

from application.requests.user import CreateUser
from application.responses.user_and_person_created import UserAndPersonCreated
from application.services.person_service import CreatePersonService
from application.services.user_service import CreateUserService
from infrastructure.database.repository.profiles.profile_repo import ProfileRepo
from libs.types.identifiers import PersonUUID, UserUUID


profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")


@profile_blueprint.route("/register", methods=["POST", "OPTIONS"])
def register_new_profile():
    data = request.get_json()
    # First of all, creating a user
    user_requester = CreateUser(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        avatar=data.get("avatar", None),
    )

    user_requester.validate_request()

    profile_repo = ProfileRepo()
    user_service = CreateUserService(requester=user_requester, repo=profile_repo)
    user = user_service.create_or_update()
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
