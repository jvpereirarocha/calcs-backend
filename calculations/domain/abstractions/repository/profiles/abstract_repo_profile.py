from abc import ABC, abstractmethod
from typing import Iterable, Optional
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from calculations.domain.entities.person import Person
from libs.types.identifiers import PersonUUID, UserUUID
from calculations.domain.entities.user import User


class AbstractProfileRepo(AbstractRepo, ABC):
    @abstractmethod
    def get_first_user(self) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        raise NotImplementedError()
    
    @abstractmethod
    def get_first_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError()
    
    @abstractmethod
    def save_user(self, user: User) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all_users(self) -> Iterable[User]:
        raise NotImplementedError()
    
    @abstractmethod
    def get_person_by_id(self, person_id: PersonUUID) -> Optional[Person]:
        raise NotImplementedError()
    
    @abstractmethod
    def get_person_by_user_email(self, email: str) -> Optional[Person]:
        raise NotImplementedError()
    
    @abstractmethod
    def save_person(self, person: Person) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()