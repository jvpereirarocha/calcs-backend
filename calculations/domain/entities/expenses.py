from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from calculations.adapters.types.basic_types import AccountUUID, ExpenseUUID, PersonUUID

from calculations.domain.entities.models import BaseModel


@dataclass
class Expense(BaseModel):
    id: Optional[ExpenseUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    due_date: Optional[datetime] = None
    already_paid: Optional[bool] = None
    account_id: Optional[AccountUUID] = None
    category: Optional[str] = None