from dataclasses import dataclass
from typing import Optional
from calculations.adapters.types.basic_types import ExpenseUUID

from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseModel:
    created_when: datetime
    modified_when: datetime

    def __post_init__(self):
        self.modified_when = datetime.now()
        self.created_when = datetime.now()