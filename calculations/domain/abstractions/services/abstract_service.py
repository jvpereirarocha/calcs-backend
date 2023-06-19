from abc import ABC, abstractmethod
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from libs.types.identifiers import BaseUUID


class AbstractCreateOrUpdateService(ABC):
    def __init__(self, requester: AbstractInputPort, repo: AbstractRepo):
        self.requester = requester
        self.repo = repo

    @abstractmethod
    def create_or_update(self):
        raise NotImplementedError()


class AbstractFetchOneService(ABC):
    def __init__(self, repo: AbstractRepo) -> None:
        self.repo = repo

    @abstractmethod
    def fetch_one(self, entity_id: BaseUUID):
        raise NotImplementedError()


class AbstractGetAllService(ABC):
    def __init__(self, repo: AbstractRepo) -> None:
        self.repo = repo

    @abstractmethod
    def get_all(self):
        raise NotImplementedError()
