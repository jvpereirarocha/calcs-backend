from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from libs.types.identifiers import UserUUID, PersonUUID
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.models import BaseModel
from calculations.domain.entities.revenues import Revenue


@dataclass
class Person(BaseModel):
    person_id: PersonUUID
    first_name: str
    last_name: str
    date_of_birth: datetime
    accounts: Optional[List[Account]] = field(default_factory=list)
    expenses: Optional[List[Expense]] = field(default_factory=list)
    revenues: Optional[List[Revenue]] = field(default_factory=list)
    user_id: Optional[UserUUID] = None
