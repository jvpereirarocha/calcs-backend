from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, Optional, List, Self

from libs.types.identifiers import UserUUID
from calculations.domain.entities.models import InheritedModel
import bcrypt
import jwt


@dataclass
class User(InheritedModel):
    user_id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None

    def __hash__(self) -> int:
        return id(self.user_id)

    @classmethod
    def encrypt_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)

    @classmethod
    def create_user(
        cls, user_id: UserUUID, email: str, password: str, avatar: Optional[str] = None
    ) -> "User":
        return cls(
            user_id=user_id,
            email=email,
            password=cls.encrypt_password(password=password),
            avatar=avatar,
            created_when=datetime.now(),
            modified_when=datetime.now(),
        )

    def update_user(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        avatar: Optional[str] = None,
    ) -> None:
        if email:
            self.email = email
        if password:
            self.password = self.encrypt_password(password=password)
        if avatar:
            self.avatar = avatar

        self.modified_when = datetime.now()

    def get_expiration_date(self) -> datetime:
        return datetime.now()

    def get_token(self, secret_key, expiration_in_minutes: int = 60) -> str:
        expiration_date = self.get_expiration_date() + timedelta(minutes=expiration_in_minutes)
        return jwt.encode(
            {
                "exp": int(expiration_date.timestamp()),
                "user_id": str(self.user_id),
                "email": self.email
            },
            key=secret_key
        )
    
    def decode_token_and_get_user_information(self, token: str, secret_key: str) -> Dict[str, str]:
        return jwt.decode(jwt=token, key=secret_key)

    def to_dict(self) -> Dict[str, str]:
        return {
            "user_id": str(self.user_id),
            "email": self.email,
            "avatar": self.avatar,
        }
