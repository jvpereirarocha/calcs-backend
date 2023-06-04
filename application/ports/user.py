from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from dataclasses import dataclass

from libs.types.identifiers import UserUUID


@dataclass
class CreateUser(AbstractInputPort):
    user_id: UserUUID
    email: str
    password: str
    avatar: str
