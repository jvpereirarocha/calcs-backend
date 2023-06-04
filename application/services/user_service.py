from typing import Iterable
from application.ports.user import CreateUser
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from calculations.domain.abstractions.repository.user.abstract_repo_user import AbstractUserRepo
from calculations.domain.abstractions.services.abstract_service import (
    AbstractCreateOrUpdateService,
    AbstractGetAllService,
    AbstractFetchOneService,
)
from calculations.domain.entities.user import User
from libs.types.identifiers import BaseUUID


class CreateUserService(AbstractCreateOrUpdateService):
    def __init__(self, requester: CreateUser, repo: AbstractUserRepo):
        self.requester = requester
        self.repo = repo
    
    def _create_new_user(self):
        user = User.create_user(
            user_id=self.requester.user_id,
            email=self.requester.email,
            password=self.requester.password,
            avatar=self.requester.avatar
        )
        self.repo.save_user(user=user)

    def create_or_update(self):
        return self._create_new_user()
    
class GetUsersService(AbstractGetAllService):
    def __init__(self, repo: AbstractUserRepo) -> None:
        self.repo = repo

    def get_all(self) -> Iterable[User]:
        return self.repo.get_all_users()
    

class FetchOneUserService(AbstractFetchOneService):
    def __init__(self, repo: AbstractUserRepo) -> None:
        self.repo = repo
    
    def fetch_one(self, entity_id: BaseUUID) -> User:
        return self.repo.get_first_user_by_id(
            user_id=entity_id
        )
    
    def get_first_user(self) -> User:
        return self.repo.get_first_user()
