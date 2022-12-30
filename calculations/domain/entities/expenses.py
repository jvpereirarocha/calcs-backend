from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from calculations.adapters.types.basic_types import ExpenseUUID, PersonUUID

from calculations.domain.entities.models import BaseModel


@dataclass
class Expense(BaseModel):
    expense_id: Optional[ExpenseUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    due_date: Optional[datetime] = None
    already_paid: Optional[bool] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None