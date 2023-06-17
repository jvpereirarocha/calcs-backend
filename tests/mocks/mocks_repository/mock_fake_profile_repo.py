from typing import Iterable, Optional, Set

from pytest import fixture
from calculations.domain.abstractions.repository.profiles.abstract_repo_profile import AbstractProfileRepo
from calculations.domain.entities.person import Person
from calculations.domain.entities.user import User
from libs.types.identifiers import PersonUUID, UserUUID


class FakeProfileRepo(AbstractProfileRepo):
    def __init__(self, data: Set[User | Person]):
        self.data = data
        self._list_of_objects = []
        self._commited = False
    
    @property
    def commited(self):
        return self._commited

    def _get_only_users_by_dataset(self) -> Set[User]:
        users = set([obj for obj in self.data if issubclass(obj.__class__, User)])
        return users
    
    def _get_only_persons_by_dataset(self) -> Set[Person]:
        persons = set([obj for obj in self.data if issubclass(obj.__class__, Person)])
        return persons

    def get_first_user(self) -> User | None:
        users = self._get_only_users_by_dataset()
        return next((user for user in users), None)
    
    def get_all_users(self) -> Iterable[User]:
        return self._get_only_users_by_dataset()
    
    def get_first_person(self) -> Person | None:
        persons = self._get_only_persons_by_dataset()
        return next((person for person in persons), None)
    
    def get_first_user_by_email(self, email: str) -> User | None:
        users = self._get_only_users_by_dataset()
        return next((user for user in users if user.email == email), None)
    
    def get_first_user_by_id(self, user_id: UserUUID) -> User | None:
        users = self._get_only_users_by_dataset()
        return next((user for user in users if user.user_id == user_id), None)
    
    def get_person_by_id(self, person_id: PersonUUID) -> Person | None:
        persons = self._get_only_persons_by_dataset()
        return next((person for person in persons if person.user_id == person_id), None)
    
    def get_person_by_user_email(self, email: str) -> Person | None:
        users = self._get_only_users_by_dataset()
        user = next((user for user in users if user.email == email), None)
        person = None
        if user:
            user_id = user.user_id
            persons = self._get_only_persons_by_dataset()
            person = next((person for person in persons if person.user_id == user_id), None)
        return person
    
    def save_user(self, user: User) -> None:
        self._list_of_objects.append(user)
    
    def save_person(self, person: Person) -> None:
        self._list_of_objects.append(person)

    def commit(self):
        for obj in self._list_of_objects:
            self.data.add(obj)
        
        self._commited = True