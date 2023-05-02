from application.ports.user import CreateUserInputPort
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from calculations.domain.abstractions.repository.user.abstract_repo_user import AbstractUserRepo
from calculations.domain.abstractions.services.abstract_service import AbstractService
from calculations.domain.entities.user import User


class CreateUserService(AbstractService):
    def __init__(self, requester: CreateUserInputPort, repo: AbstractUserRepo):
        super().__init__(requester, repo)

    def _create_new_user(self):
        user = User.create_user(
            user_id=self.requester.user_id,
            email=self.requester.email,
            password=self.requester.password,
            avatar=self.requester.avatar
        )
        self.repo.save_user(user=user)

    def operation(self):
        return self._create_new_user()