import pytest
import random
from typing import Optional
from datetime import datetime
from calculations.adapters.types.basic_types import PersonUUID
from calculations.domain.entities.person import Person

@pytest.fixture(scope="function")
def mock_person_generate():

    def make_mock(
        id: Optional[PersonUUID] = None,
        name: Optional[str] = None,
        date_of_birth: Optional[datetime] = None,
        modified_when: Optional[datetime] = None
    ):
        person = Person(
            id=id or PersonUUID(),
            name=name or random.choice(["person 1", "person 2", "person"]),
            date_of_birth=date_of_birth or datetime.now(),
            created_when=datetime.now(),
            modified_when=modified_when or datetime.now()
        )

        return person

    yield make_mock


@pytest.fixture(scope="function")
def mock_person(mock_person_generate):
    yield mock_person_generate()