from typing import Optional
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from dataclasses import dataclass

from libs.types.identifiers import UserUUID


@dataclass
class CreateUser(AbstractInputPort):
    user_id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None

    def _validate_email(self):
        if not self.email:
            raise ValueError("Email is required.")
        
    def _validate_password(self):
        if not self.password:
            raise ValueError("Password is required.")

    def validate_request(self):
        self._validate_email()
        self._validate_password()
