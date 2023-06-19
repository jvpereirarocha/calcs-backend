from datetime import datetime
import pytest
import random
from typing import Optional
from libs.types.identifiers import ExpenseUUID
from calculations.domain.entities.expenses import Expense
from calculations.domain.value_object.expense_category import ExpenseCategory


@pytest.fixture(scope="function")
def mock_expense_generate(mock_account):
    def make_mock(
        id: Optional[ExpenseUUID] = None,
        description: Optional[str] = None,
        value: Optional[float] = None,
        due_date: Optional[datetime] = None,
        already_paid: Optional[bool] = None,
        modified_when: Optional[datetime] = None,
    ):
        expense = Expense(
            expense_id=id or ExpenseUUID(),
            description=description
            or random.choice(["expense 1", "expense 2", "expense 3"]),
            value=value or random.uniform(0.0, 100.0),
            due_date=due_date or datetime.now(),
            already_paid=already_paid or random.choice([True, False]),
            account_used_on_payment=mock_account,
            category=random.choice(
                [
                    ExpenseCategory.food,
                    ExpenseCategory.entertainment,
                    ExpenseCategory.health,
                    ExpenseCategory.other,
                    ExpenseCategory.transport,
                ]
            ),
            created_when=datetime.now(),
            modified_when=modified_when or datetime.now(),
        )

        return expense

    yield make_mock


@pytest.fixture(scope="function")
def mock_expense(mock_expense_generate):
    yield mock_expense_generate()
