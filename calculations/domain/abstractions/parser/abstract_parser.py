from abc import ABC, abstractmethod
from typing import Iterable, List, Optional, Union

from calculations.domain.entities.models import BaseModel

class AbstractParser(ABC):
    
    @abstractmethod
    def to_json(self, data: Union[BaseModel, Iterable[BaseModel], None] = None) -> List[str] | str:
        raise NotImplementedError()
