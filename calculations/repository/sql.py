import uuid
from calculations.repository.base import BaseRepo
from calculations.domain.entities.user import User


class SqlAlchemyRepo(BaseRepo):
    def consultar_primeiro_usuario(self) -> User:
        with self:
            return self.session.query(User).first()
