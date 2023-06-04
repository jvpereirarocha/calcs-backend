from abc import ABC, abstractmethod
from typing import Iterable, Optional
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from libs.types.identifiers import PersonUUID
from calculations.domain.entities.person import Person


class AbstractPersonRepo(AbstractRepo, ABC):
    @abstractmethod
    def get_first_person(self) -> Optional[Person]:
        raise NotImplementedError()

    @abstractmethod
    def get_first_person_by_id(self, person_id: PersonUUID) -> Optional[Person]:
        raise NotImplementedError()
    
    @abstractmethod
    def save_person(self, person: Person) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all_persons(self) -> Iterable[Person]:
        raise NotImplementedError()
    
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()