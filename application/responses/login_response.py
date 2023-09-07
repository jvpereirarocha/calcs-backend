import json
from typing import List
from calculations.domain.abstractions.port.abstract_port import AbstractOutputPort


class LoginResponse(AbstractOutputPort):
    def __init__(self, email: str, token: str, error: str = ""):
        self.email = email
        self.token = token
        self.error = error
        self.status_code = None

    def to_json(self):
        try:
            if not self.error:
                data = {
                    "email": self.email,
                    "token": self.token,
                }
                self.success = data
                self.status_code = 200
            else:
                self.status_code = 400
        except Exception as error:
            self.status_code = 400
            self.error = error

        return self.build_response(), self.status_code
