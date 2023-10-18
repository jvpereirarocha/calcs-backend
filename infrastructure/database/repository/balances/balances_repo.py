from typing import Optional, Set

from sqlalchemy import select
from calculations.domain.abstractions.repository.balances.abstract_repo_balance import (
    AbstractBalanceRepo,
)
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue
from infrastructure.database.repository.base import SqlBaseRepo


class BalanceRepo(SqlBaseRepo, AbstractBalanceRepo):
    def __init__(self):
        super().__init__()
        self.objects_of_expenses: Set[Expense] = set()
        self.objects_of_revenues: Set[Revenue] = set()
        self.balance_to_save: Balance | None = None

    def get_balance_by_month_and_year(self, month: int, year: int) -> Optional[Balance]:
        with self:
            query = (
                select(Balance, Expense)
                .join(Balance.expenses)
                .where(Balance.month == month, Balance.year == year)
            )
            balance = self.session.execute(query).scalar_one_or_none()

        return balance

    def save_balance(self, balance: Balance) -> None:
        revenues = balance.revenues
        expenses = balance.expenses
        self.objects_of_revenues.update(revenues)
        self.objects_of_expenses.update(expenses)
        self.balance_to_save = balance

    def add_revenue(self, revenue: Revenue) -> None:
        self.objects_of_revenues.add(revenue)

    def add_expense(self, expense: Expense) -> None:
        self.objects_of_expenses.add(expense)

    def commit(self):
        with self:
            self.session.add(self.balance_to_save)
            self.session.commit()
