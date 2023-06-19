import json
from calculations.domain.abstractions.port.abstract_port import AbstractOutputPort
from calculations.domain.entities.person import Person
from calculations.domain.entities.user import User


class UserAndPersonCreated(AbstractOutputPort):
    def __init__(self, person: Person, user: User):
        self.person = person
        self.user = user
        self.status_code = 200

    def to_json(self):
        try:
            data = {
                "success": {
                    "person": self.person.to_dict(),
                    "user": self.user.to_dict()
                }
            }
            serialized_data = json.dumps(data)
            self.status_code = 201
            return serialized_data, self.status_code
        except Exception as error:
            self.status_code = 400
            return json.dumps({
                "error": {
                    "message": str(error)
                }
            }), self.status_code