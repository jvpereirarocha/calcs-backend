from flask import Blueprint, jsonify, request
from application.input_ports.person import CreatePerson

from application.input_ports.user import CreateUser
from application.output_ports.user_and_person_created import UserAndPersonCreated
from application.services.person_service import CreatePersonService
from application.services.user_service import CreateUserService
from infrastructure.database.repository.persons.person_repo import PersonRepo
from infrastructure.database.repository.users.user_repo import UserRepo
from libs.types.identifiers import PersonUUID, UserUUID


user_blueprint = Blueprint("users", __name__, url_prefix="/users")

@user_blueprint.route("/new", methods=["POST", "OPTIONS"])
def create_user_and_person():
    data = request.get_json()
    # First of all, creating a user
    user_data = CreateUser(
        user_id=UserUUID(),
        email=data["email"],
        password=data["password"],
        avatar=data.get("avatar", None)
    )
    
    user_repo = UserRepo()
    user_service = CreateUserService(requester=user_data, repo=user_repo)
    user = user_service.create_or_update()
    user_repo.commit()
    # After that, creating a person instance
    person_requester = CreatePerson(
        person_id=PersonUUID(),
        first_name=data["first_name"],
        last_name=data["last_name"],
        date_of_birth=data["date_of_birth"]
    )

    person_repo = PersonRepo()
    person_service = CreatePersonService(requester=person_requester, repo=person_repo)
    person = person_service.create_or_update()
    person_repo.commit()

    response = UserAndPersonCreated(
        user=user,
        person=person
    )
    return jsonify(response.to_json()), response.status_code
