from typing import Optional
from application.requests.mixins import UserValidatorMixin
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from dataclasses import dataclass

from libs.types.identifiers import UserUUID


@dataclass
class CreateUser(AbstractInputPort, UserValidatorMixin):
    user_id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None

    _valid_request: bool = False

    def validate_request(self):
        self.validate_email()
        self.validate_password()
        self._valid_request = True

    def request_is_valid(self):
        return self._valid_request
    

@dataclass
class LoginRequest(AbstractInputPort, UserValidatorMixin):
    email: str
    password: str

    _validate_request: bool = False

    def validate_login(self):
        self.validate_email()
        self.validate_password()
        self._validate_request = True
    
    def request_is_valid(self):
        return self._validate_request
