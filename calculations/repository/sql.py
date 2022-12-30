from typing import Optional
import uuid
from calculations.adapters.types.basic_types import UserUUID
from calculations.repository.base import BaseRepo
from calculations.domain.entities.user import User


class SqlAlchemyRepo(BaseRepo):
    def consultar_primeiro_usuario(self) -> Optional[User]:
        with self:
            return self.session.query(User).first()

    def consultar_usuario_por_id(self, usuario_id: UserUUID) -> Optional[User]:
        with self:
            return self.session.query(User.user_id == usuario_id).first()
