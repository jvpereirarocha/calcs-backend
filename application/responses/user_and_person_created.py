import json
from calculations.domain.abstractions.port.abstract_port import AbstractOutputPort
from calculations.domain.entities.person import Person
from calculations.domain.entities.user import User


class UserAndPersonCreated(AbstractOutputPort):
    def __init__(self, person: Person, user: User, error: str = ""):
        self.person = person
        self.user = user
        self.status_code = 200
        self.error = error

    def to_json(self):
        try:
            self.success = "user saved"
            self.status_code = 201
            data = {"success": self.success}, self.status_code
        except Exception as error:
            self.error = error
            self.status_code = 400
            data = {"error": self.error}, self.status_code
            # return json.dumps({"error": {"message": str(error)}}), self.status_code

        return self.build_response(), self.status_code
