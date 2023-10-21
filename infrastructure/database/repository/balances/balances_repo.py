from typing import Optional, Set

from sqlalchemy import select
from calculations.domain.abstractions.repository.balances.abstract_repo_balance import (
    AbstractBalanceRepo,
)
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue
from infrastructure.database.repository.base import SqlBaseRepo
from libs.types.identifiers import ExpenseUUID


class BalanceRepo(SqlBaseRepo, AbstractBalanceRepo):
    def __init__(self):
        super().__init__()
        self.expenses_to_save: Set[Expense] = set()
        self.revenues_to_save: Set[Revenue] = set()
        self.balance_to_save: Balance | None = None
        self.revenues_to_delete: Set[Revenue] = set()
        self.expenses_to_delete: Set[Expense] = set()

    def get_balance_by_month_and_year(self, month: int, year: int) -> Optional[Balance]:
        with self:
            query = select(Balance).where(Balance.month == month, Balance.year == year)
            balance = self.session.execute(query).scalar_one_or_none()

        return balance

    def get_expense_by_id(self, expense_id: str) -> Optional[Expense]:
        with self:
            query = select(Expense).where(Expense.expense_id == ExpenseUUID(expense_id))
            expense = self.session.execute(query).scalar_one_or_none()

        return expense

    def remove_expense(self, expense: Expense) -> None:
        self.expenses_to_delete.add(expense)

    def save_balance(self, balance: Balance) -> None:
        revenues = balance.revenues
        expenses = balance.expenses
        self.revenues_to_save.update(revenues)
        self.expenses_to_save.update(expenses)
        self.balance_to_save = balance

    def add_revenue(self, revenue: Revenue) -> None:
        self.revenues_to_save.add(revenue)

    def add_expense(self, expense: Expense) -> None:
        self.expenses_to_save.add(expense)

    def commit(self):
        with self:
            if self.balance_to_save:
                self.session.add(self.balance_to_save)
            if self.expenses_to_delete:
                for expense in self.expenses_to_delete:
                    self.session.delete(expense)
            if self.revenues_to_delete:
                for revenue in self.revenues_to_delete:
                    self.session.delete(revenue)

            self.session.commit()
