from datetime import datetime
from abc import ABC, abstractmethod


class AbstractInputPort(ABC):
    def __init__(self, created_at: datetime = datetime.now()) -> None:
        self.created_at = created_at

    @abstractmethod
    def validate_request(self):
        raise NotImplementedError()
    
    @abstractmethod
    def request_is_valid(self):
        raise NotImplementedError()
    

class AbstractOutputPort(ABC):
    def __init__(self) -> None:
        self.status_code = 200
    
    @abstractmethod
    def to_json(self, data):
        raise NotImplementedError()