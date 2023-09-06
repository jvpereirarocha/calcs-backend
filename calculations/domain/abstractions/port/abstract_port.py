from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict
import json


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
        self.error = ''
        self.success = ''
        self._data = {}

    @abstractmethod
    def to_json(self, data):
        raise NotImplementedError()
    
    def build_response(self) -> Dict[str, str]:
        if self.error:
            self._data = {"error": self.error}
        elif self.success:
            self._data = {"success": self.success}

        return json.dumps(self._data)
