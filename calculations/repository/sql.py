from typing import Optional
from calculations.adapters.types.basic_types import UserUUID
from calculations.repository.base import BaseRepo
from calculations.domain.entities.user import User


class SqlAlchemyRepo(BaseRepo):
    def get_first_user(self) -> Optional[User]:
        with self:
            return self.session.query(User).first()

    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        with self:
            return self.session.query(User.user_id == user_id).first()
