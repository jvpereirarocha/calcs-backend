from datetime import datetime
from pytest import mark


def test_creating_new_expense(mock_expense_generate):

    expense = mock_expense_generate(
        description="Market",
        value=300.00,
        due_date=datetime(2023, 6, 30),
        already_paid=True
    )

    assert expense is not None