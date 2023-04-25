from abc import ABC
from typing import Optional
from calculations.adapters.types.basic_types import UserUUID
from calculations.domain.entities.user import User


class AbstractUserRepo(ABC):
    def get_first_user(self) -> Optional[User]:
        raise NotImplementedError()

    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        raise NotImplementedError()