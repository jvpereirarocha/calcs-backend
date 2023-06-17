import pytest
import random
from typing import Optional
from datetime import datetime
from libs.types.identifiers import UserUUID
from calculations.domain.entities.user import User


@pytest.fixture(scope="function")
def mock_user_generate():

    def make_mock(
        id: Optional[UserUUID] = None,
        email: Optional[str] = None,
        modified_when: Optional[datetime] = None
    ):
        user = User(
            user_id=id or UserUUID(),
            email=email or random.choice(["user1@gmail.com", "user2@gmail.com", "user3@gmail.com"]),
            password=random.choice([
                "password1",
                "password2",
                "password3"
            ]),
            avatar="https://google.com",
            created_when=datetime.now(),
            modified_when=modified_when or datetime.now()
        )

        return user

    yield make_mock


@pytest.fixture(scope="function")
def mock_user(mock_user_generate):
    yield mock_user_generate()