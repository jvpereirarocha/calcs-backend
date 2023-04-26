from abc import ABC, abstractmethod
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo


class AbstractService(ABC):
    def __init__(self, requester: AbstractInputPort, repo: AbstractRepo):
        self.requester = requester
        self.repo = repo

    @abstractmethod
    def operation(self):
        raise NotImplementedError()