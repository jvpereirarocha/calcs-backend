from dataclasses import dataclass
from datetime import datetime

from calculations.adapters.types.basic_types import PersonUUID


@dataclass
class Person:
    id: PersonUUID
    name: str
    date_of_birth: datetime
