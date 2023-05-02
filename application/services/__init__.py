from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from calculations.domain.abstractions.services.abstract_service import AbstractService
from calculations.domain.entities.user import User


class UserService(AbstractService):
    def __init__(self, requester: AbstractInputPort, repo: AbstractRepo):
        super().__init__(requester, repo)

    def _create_new_user(self):
        new_user = 

    def operation(self):
        return super().operation()