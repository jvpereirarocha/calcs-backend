from typing import Iterable, Optional

from sqlalchemy import select
from libs.types.identifiers import UserUUID
from calculations.domain.abstractions.repository.user.abstract_repo_user import AbstractUserRepo
from calculations.domain.entities.user import User
from infrastructure.database.repository.base import SqlBaseRepo


class UserRepo(SqlBaseRepo, AbstractUserRepo):
    def get_first_user(self) -> Optional[User]:
        with self:
            query = select(User).order_by(User.email)
            return self.session.execute(query).scalar_one_or_none()

    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        with self:
            query = select(User).where(User.user_id == user_id)
            return self.session.execute(query).scalar_one_or_none()
        
    def get_first_by_email(self, email: str) -> Optional[User]:
        with self:
            query = select(User).where(User.email == email)
            return self.session.execute(query).scalar_one_or_none()
        
    def save_user(self, user: User) -> None:
        with self:
            self.session.add(user)
            self.session.commit()

    def get_all_users(self) -> Iterable[User]:
        with self:
            query = select(User).order_by(User.email)
            return self.session.execute(query).scalars()
        
    def commit(self) -> None:
        with self:
            self.session.commit()