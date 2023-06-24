import json
from typing import List
from calculations.domain.abstractions.port.abstract_port import AbstractOutputPort


class LoginResponse(AbstractOutputPort):
    def __init__(self, email: str, token: str, errors: List[str] = []):
        self.email = email
        self.token = token
        self.errors = errors
        self.status_code = None

    def to_json(self):
        try:
            if not self.errors:
                data = {
                    "email": self.email,
                    "token": self.token,
                }
                self.status_code = 200
            else:
                data = {
                    "errors": [error for error in self.errors] 
                }
                self.status_code = 400
            serialized_data = json.dumps(data)
            return serialized_data, self.status_code
        except Exception as error:
            self.status_code = 400
            return json.dumps({"error": {"message": str(error)}}), self.status_code
