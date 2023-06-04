from typing import Iterable, Optional
from calculations.domain.entities.person import Person
from libs.types.identifiers import UserUUID
from calculations.domain.abstractions.repository.person.abstract_repo_person import AbstractPersonRepo
from calculations.domain.entities.user import User
from infrastructure.database.repository.base import SqlBaseRepo


class PersonRepo(SqlBaseRepo, AbstractPersonRepo):
    def get_first_person(self) -> Person | None:
        with self:
            return self.session.query(Person).first()
        
    def get_first_person_by_id(self, person_id: UserUUID) -> Person | None:
        with self:
            return self.session.query(Person.person_id == person_id).first()
        
    def save_person(self, person: Person) -> None:
        with self:
            self.session.add(person)

    def get_all_persons(self) -> Iterable[Person]:
        with self:
            return self.session.query(Person).all()
        
    def commit(self) -> None:
        with self:
            self.session.commit()