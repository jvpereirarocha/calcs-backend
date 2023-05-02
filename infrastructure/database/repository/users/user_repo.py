from typing import Iterable, Optional
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
        
    def save_user(self, user: User) -> None:
        with self:
            self.session.add(user)
            self.session.commit()

    def get_all_users(self) -> Iterable[User]:
        with self:
            return self.session.query(User).all()