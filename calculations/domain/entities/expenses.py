from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Self
from calculations.domain.value_object.expense_category import ExpenseCategory
from libs.types.identifiers import ExpenseUUID, PersonUUID, BalanceUUID

from calculations.domain.entities.models import InheritedModel


@dataclass
class Expense(InheritedModel):
    expense_id: Optional[ExpenseUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    due_date: Optional[datetime] = None
    already_paid: Optional[bool] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None
    balance_id: Optional[BalanceUUID] = None

    @classmethod
    def create_new_expense(
        cls,
        description: str,
        value: float,
        due_date: datetime,
        person_id: PersonUUID,
        category: str,
        balance_id: BalanceUUID,
        already_paid: bool = False,
    ) -> Self:

        return cls(
            expense_id=ExpenseUUID(),
            description=description,
            value=value,
            due_date=due_date,
            already_paid=already_paid,
            person_id=person_id,
            category=category,
            balance_id=balance_id
        )
