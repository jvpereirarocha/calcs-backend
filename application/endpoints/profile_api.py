from flask import Blueprint, jsonify, request
from application.input_ports.person import CreatePerson

from application.input_ports.user import CreateUser
from application.output_ports.user_and_person_created import UserAndPersonCreated
from application.services.person_service import CreatePersonService
from application.services.user_service import CreateUserService
from infrastructure.database.repository.profiles.profile_repo import ProfileRepo
from libs.types.identifiers import PersonUUID, UserUUID


profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")

@profile_blueprint.route("/register", methods=["POST", "OPTIONS"])
def register_new_profile():
    data = request.get_json()
    # First of all, creating a user
    user_data = CreateUser(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        avatar=data.get("avatar", None)
    )
    
    profile_repo = ProfileRepo()
    user_service = CreateUserService(requester=user_data, repo=profile_repo)
    user = user_service.create_or_update()
    # After that, creating a person instance
    person_requester = CreatePerson(
        person_id=PersonUUID(),
        first_name=data["first_name"],
        last_name=data["last_name"],
        date_of_birth=data["date_of_birth"]
    )

    person_service = CreatePersonService(requester=person_requester, repo=profile_repo)
    person = person_service.create_or_update()
    
    profile_repo.commit()

    response = UserAndPersonCreated(
        user=user,
        person=person
    )
    return jsonify(response.to_json()), response.status_code
