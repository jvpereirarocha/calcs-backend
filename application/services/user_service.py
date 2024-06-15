from typing import Dict, Iterable, List, Optional
from application.requests.user import CreateUser, LoginRequest
from calculations.domain.abstractions.repository.profiles.abstract_repo_profile import (
    AbstractProfileRepo,
)
from calculations.domain.abstractions.services.abstract_service import (
    AbstractCreateOrUpdateService,
    AbstractGetAllService,
    AbstractFetchOneService,
)
from calculations.domain.entities.user import User
from libs.types.identifiers import BaseUUID, UserUUID
from os import getenv


class CreateUserService(AbstractCreateOrUpdateService):
    def __init__(self, requester: CreateUser, repo: AbstractProfileRepo):
        self.requester = requester
        self.repo = repo
        self.error = ""
        self.user = None

    def _validate_new_user(self):
        user_can_be_created = True
        user_already_exists = self.repo.get_first_user_by_email(
            email=self.requester.email
        )
        if user_already_exists:
            self.error = "Um usuário com esse e-mail já foi cadastrado!"
            user_can_be_created = False

        return user_can_be_created

    def _create_new_user(self):
        user = User.create_user(
            user_id=self.requester.user_id,
            email=self.requester.email,
            password=self.requester.password,
            avatar=self.requester.avatar,
        )
        self.repo.save_user(user=user)
        self.user = user
        return self

    def create_or_update(self):
        user_is_valid_an_can_be_created = self._validate_new_user()
        if not user_is_valid_an_can_be_created:
            return self

        return self._create_new_user()


class LoginService(AbstractFetchOneService):
    def __init__(self, requester: LoginRequest, repo: AbstractProfileRepo, error: str):
        self.requester = requester
        self.repo = repo
        self.error = error

    def fetch_one(self, entity_id: UserUUID) -> Optional[User]:
        return self.repo.get_first_user_by_id(user_id=entity_id)

    def fetch_by_email(self) -> Optional[User]:
        return self.repo.get_first_user_by_email(email=self.requester.email)

    def make_login(self) -> Optional[str]:
        user: Optional[User] = self.fetch_by_email()
        if (
            user
            and user.email == self.requester.email
            and user.check_password(password_to_verify=self.requester.password)
        ):
            return user.get_token(secret_key=getenv("JWT_SECRET_KEY"))
        else:
            error = "Credencial inválida"
            self.error = error

    @classmethod
    def check_token(cls, token: str) -> Dict[str, str]:
        return User.decode_token_and_get_user_information(
            token=token, secret_key=getenv("JWT_SECRET_KEY")
        )


class GetUsersService(AbstractGetAllService):
    def __init__(self, repo: AbstractProfileRepo) -> None:
        self.repo = repo

    def get_all(self) -> Iterable[User]:
        return self.repo.get_all_users()


class FetchOneUserService(AbstractFetchOneService):
    def __init__(self, repo: AbstractProfileRepo) -> None:
        self.repo = repo

    def fetch_one(self, entity_id: BaseUUID) -> User:
        return self.repo.get_first_user_by_id(user_id=entity_id)

    def get_first_user(self) -> User:
        return self.repo.get_first_user()
