from dataclasses import dataclass
from datetime import datetime

from calculations.domain.abstractions.port.abstract_port import AbstractInputPort


@dataclass
class CreateOrUpdateRevenue(AbstractInputPort):
    description: str
    value: float
    date_of_receivment: datetime
    category: str
