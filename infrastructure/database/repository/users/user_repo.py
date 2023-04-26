from typing import Optional
from libs.types.identifiers import UserUUID
from calculations.domain.abstractions.repository.user.abstract_repo_user import AbstractUserRepo
from calculations.domain.entities.user import User
from infrastructure.database.repository.base import SqlBaseRepo


class UserRepo(SqlBaseRepo, AbstractUserRepo):
    def get_first_user(self) -> Optional[User]:
        with self:
            return self.session.query(User).first()

    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        with self:
            return self.session.query(User.user_id == user_id).first()