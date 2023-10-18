from dataclasses import dataclass
from datetime import datetime

from calculations.domain.abstractions.port.abstract_port import AbstractInputPort


@dataclass
class CreateOrUpdateExpense(AbstractInputPort):
    description: str
    value: float
    due_date: datetime
    already_paid: bool
    category: str
