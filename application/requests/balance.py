from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from application.requests.expenses import CreateOrUpdateExpense
from application.requests.revenues import CreateOrUpdateRevenue

from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from calculations.domain.aggregates.balance import StatusBalance
from libs.types.identifiers import PersonUUID


@dataclass
class CreateOrUpdateBalance(AbstractInputPort):
    person_id: PersonUUID
    month: int
    year: int
    status_balance: str = StatusBalance.INITIAL.value
    expense: Optional[List[CreateOrUpdateExpense]] = None
    revenue: Optional[List[CreateOrUpdateRevenue]] = None
    created_when: datetime = datetime.now()
    modified_when: datetime = datetime.now()
