from abc import ABC, abstractmethod
from typing import Iterable, Optional
from libs.types.identifiers import UserUUID
from calculations.domain.entities.user import User


class AbstractUserRepo(ABC):
    @abstractmethod
    def get_first_user(self) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        raise NotImplementedError()
    
    @abstractmethod
    def save_user(self, user: User) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all_users(self) -> Iterable[User]:
        raise NotImplementedError()