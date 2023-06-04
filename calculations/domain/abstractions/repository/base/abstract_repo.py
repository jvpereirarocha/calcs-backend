from abc import ABC, abstractmethod


class AbstractRepo(ABC):
    
    @abstractmethod
    def commit(self) -> None:
        pass