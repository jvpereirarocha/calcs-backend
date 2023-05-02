from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Self

from libs.types.identifiers import UserUUID
from calculations.domain.entities.models import BaseModel
import bcrypt


@dataclass
class User(BaseModel):
    user_id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None

    @classmethod
    def _encrypt_password(self, password: str) -> str:
        salt = bcrypt.gensalt(rounds=32)
        return bcrypt.hashpw(password=password, salt=salt)

    @classmethod
    def create_user(cls, user_id: UserUUID, email: str, password: str, avatar: Optional[str] = None) -> Self:
        return cls(
            user_id=user_id,
            email=email,
            password=cls._encrypt_password(password=password),
            avatar=avatar
        )
