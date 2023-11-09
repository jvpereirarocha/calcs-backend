from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, Optional, List, Self

from libs.types.identifiers import UserUUID
from calculations.domain.entities.models import InheritedModel
import bcrypt
import jwt


@dataclass
class User(InheritedModel):
    user_id: Optional[UserUUID] = None
    email: Optional[str] = ""
    password_hash: Optional[bytes] = None
    password_salt: Optional[bytes] = None
    avatar: Optional[str] = None

    def __hash__(self) -> int:
        return id(self.user_id)

    @classmethod
    def encrypt_password(cls, password: str) -> tuple[bytes, bytes]:
        salt = bcrypt.gensalt()
        generated_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)
        return generated_password, salt

    @classmethod
    def create_user(
        cls, user_id: UserUUID, email: str, password: str, avatar: Optional[str] = None
    ) -> "User":
        password_hash, password_salt = cls.encrypt_password(password=password)
        return cls(
            user_id=user_id,
            email=email,
            password_hash=password_hash,
            password_salt=password_salt,
            avatar=avatar,
            created_when=datetime.now(),
            modified_when=datetime.now(),
        )

    def check_password(self, password_to_verify: str, encode: str = "utf-8") -> bool:
        return bcrypt.checkpw(password_to_verify.encode("utf-8"), self.password_hash)

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
        expiration_date = self.get_expiration_date() + timedelta(
            minutes=expiration_in_minutes
        )
        return jwt.encode(
            {
                "exp": int(expiration_date.timestamp()),
                "user_id": str(self.user_id),
                "email": self.email,
            },
            key=secret_key,
            algorithm="HS256",
        )

    @classmethod
    def decode_token_and_get_user_information(
        cls, token: str, secret_key: str
    ) -> Dict[str, str]:
        result = jwt.decode(jwt=token, key=secret_key, algorithms=["HS256"])
        return result

    def to_dict(self) -> Dict[str, str]:
        return {
            "user_id": str(self.user_id),
            "email": self.email,
            "avatar": self.avatar,
        }
