from calculations.domain.entities.expenses import Expense


def test_expense_dataclass(mock_expense):
    expense: Expense = mock_expense
    assert expense is not None