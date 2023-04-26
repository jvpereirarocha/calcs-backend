import pytest
import random
from typing import Optional
from datetime import datetime
from libs.types.identifiers import UserUUID
from calculations.domain.entities.user import User
import bcrypt


def _generate_password(password: str):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password

@pytest.fixture(scope="function")
def mock_user_generate():

    def make_mock(
        id: Optional[UserUUID] = None,
        email: Optional[str] = None,
        modified_when: Optional[datetime] = None
    ):
        user = User(
            id=id or UserUUID(),
            email=email or random.choice(["user1@gmail.com", "user2@gmail.com", "user3@gmail.com"]),
            password=_generate_password(
                password=random.choice([
                    "password1",
                    "password2",
                    "password3"
                ])
            ),
            avatar="https://google.com",
            modified_when=modified_when or datetime.now()
        )

        return user

    yield make_mock


@pytest.fixture(scope="function")
def mock_user(mock_user_generate):
    yield mock_user_generate()