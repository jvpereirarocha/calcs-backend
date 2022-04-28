from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from calculations.adapters.types.basic_types import BalanceUUID, PersonUUID
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.models import BaseModel
from calculations.domain.entities.revenues import Revenue


@dataclass
class Person(BaseModel):
    id: PersonUUID
    name: str
    date_of_birth: datetime
    accounts: Optional[List[Account]] = field(default_factory=list)
    expenses: Optional[List[Expense]] = field(default_factory=list)
    revenues: Optional[List[Revenue]] = field(default_factory=list)
