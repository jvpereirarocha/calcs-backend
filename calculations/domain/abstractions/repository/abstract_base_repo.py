from abc import ABC, abstractmethod


class AbstractBaseRepo(ABC):
    def __init__(self, session):
        self._session = session

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()
    
    @abstractmethod
    def __exit__(self, type_, value, traceback):
        raise NotImplementedError()