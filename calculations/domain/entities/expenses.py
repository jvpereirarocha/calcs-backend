from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from calculations.adapters.types.basic_types import ExpenseUUID
from calculations.domain.entities.accounts import Account

from calculations.domain.entities.models import BaseModel


@dataclass
class Expense(BaseModel):
    id: Optional[ExpenseUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    due_date: Optional[datetime] = None
    already_paid: Optional[bool] = None
    account_used_on_payment: Optional[Account] = None
    category: Optional[str] = None