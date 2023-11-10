from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Self, Union
from calculations.domain.value_object.format import format_to_value, format_to_date
from libs.types.identifiers import ExpenseUUID, PersonUUID, BalanceUUID

from calculations.domain.entities.models import InheritedModel


ExpenseType = Union[str, float, datetime, bool]


@dataclass
class Expense(InheritedModel):
    expense_id: Optional[ExpenseUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    due_date: Optional[date] = None
    already_paid: Optional[bool] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None
    balance_id: Optional[BalanceUUID] = None

    def __hash__(self) -> int:
        return hash(self.expense_id)

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
            balance_id=balance_id,
        )

    def check_if_attribute_was_updated_and_return_the_most_recent(
        self, old_value: ExpenseType, new_value: ExpenseType
    ) -> ExpenseType:
        if new_value:
            return new_value
        return old_value

    def update_expense(
        self,
        description: Optional[str] = None,
        value: Optional[float] = None,
        due_date: Optional[datetime] = None,
        already_paid: Optional[bool] = None,
        category: Optional[str] = None,
    ) -> Self:
        self.description = (
            self.check_if_attribute_was_updated_and_return_the_most_recent(
                self.description, description
            )
        )
        self.value = self.check_if_attribute_was_updated_and_return_the_most_recent(
            self.value, value
        )
        self.due_date = self.check_if_attribute_was_updated_and_return_the_most_recent(
            self.due_date, due_date
        )
        self.already_paid = (
            self.check_if_attribute_was_updated_and_return_the_most_recent(
                self.already_paid, already_paid
            )
        )
        self.category = self.check_if_attribute_was_updated_and_return_the_most_recent(
            self.category, category
        )
        self.modified_when = datetime.now()
        return self

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "value": format_to_value(value=self.value),
            "dueDate": format_to_date(date_as_object=self.due_date),
            "alreadyPaid": self.already_paid,
            "category": self.category,
        }
