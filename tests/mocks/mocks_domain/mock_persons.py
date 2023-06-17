import pytest
import random
from typing import Optional
from datetime import datetime
from libs.types.identifiers import PersonUUID, UserUUID
from calculations.domain.entities.person import Person

@pytest.fixture(scope="function")
def mock_person_generate():

    def make_mock(
        id: Optional[PersonUUID] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        date_of_birth: Optional[datetime] = None,
        user_id: Optional[UserUUID] = None
    ):
        person = Person(
            person_id=id or PersonUUID(),
            first_name=first_name or random.choice(["person 1", "person 2", "person"]),
            last_name=last_name or random.choice(["person 1", "person 2", "person"]),
            user_id=user_id or UserUUID(),
            date_of_birth=date_of_birth or datetime.now(),
            created_when=datetime.now(),
            modified_when=datetime.now()
        )

        return person

    yield make_mock


@pytest.fixture(scope="function")
def mock_person(mock_person_generate):
    yield mock_person_generate()