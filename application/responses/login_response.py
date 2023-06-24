import json
from calculations.domain.abstractions.port.abstract_port import AbstractOutputPort


class LoginResponse(AbstractOutputPort):
    def __init__(self, email: str, token: str):
        self.email = email
        self.token = token
        self.status_code = 200

    def to_json(self):
        try:
            data = {
                "email": self.email,
                "token": self.token,
            }
            serialized_data = json.dumps(data)
            return serialized_data, self.status_code
        except Exception as error:
            self.status_code = 400
            return json.dumps({"error": {"message": str(error)}}), self.status_code
