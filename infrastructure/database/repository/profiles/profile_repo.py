from typing import Iterable, List, Optional

from sqlalchemy import select
from calculations.domain.entities.models import InheritedModel
from calculations.domain.entities.person import Person
from libs.types.identifiers import PersonUUID, UserUUID
from calculations.domain.abstractions.repository.profiles.abstract_repo_profile import (
    AbstractProfileRepo,
)
from calculations.domain.entities.user import User
from infrastructure.database.repository.base import SqlBaseRepo


class ProfileRepo(SqlBaseRepo, AbstractProfileRepo):
    def __init__(self):
        super().__init__()
        self.objects_to_save: List[InheritedModel] = []

    def get_first_user(self) -> Optional[User]:
        with self:
            query = select(User).order_by(User.email)
            return self.session.execute(query).scalar_one_or_none()

    def get_first_user_by_id(self, user_id: UserUUID) -> Optional[User]:
        with self:
            query = select(User).where(User.user_id == user_id)
            return self.session.execute(query).scalar_one_or_none()

    def get_first_user_by_email(self, email: str) -> Optional[User]:
        with self:
            query = select(User).where(User.email == email)
            return self.session.execute(query).scalar_one_or_none()

    def save_user(self, user: User) -> None:
        with self:
            self.objects_to_save.append(user)

    def get_all_users(self) -> Iterable[User]:
        with self:
            query = select(User).order_by(User.email)
            return self.session.execute(query).scalars()

    def get_first_person(self):
        with self:
            query = select(Person).order_by(Person.first_name)
            return self.session.execute(query).scalar_one_or_none()

    def save_person(self, person: Person) -> None:
        with self:
            self.objects_to_save.append(person)

    def get_person_by_id(self, person_id: PersonUUID) -> Person | None:
        with self:
            query = select(Person).where(Person.person_id == person_id)
            return self.session.execute(query).scalar_one_or_none()

    def get_person_by_user_email(self, email: str) -> Person | None:
        with self:
            user = self.get_first_user_by_email(email=email)
            if user:
                query = select(Person).where(Person.user_id == user.user_id)
                return self.session.execute(query).scalar_one_or_none()

    def commit(self):
        with self:
            self.session.bulk_save_objects(self.objects_to_save)
            self.session.commit()
