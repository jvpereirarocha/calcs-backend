from datetime import date
from typing import Iterable, Optional, Set

from sqlalchemy import select
from calculations.domain.abstractions.repository.balances.abstract_repo_balance import (
    AbstractBalanceRepo,
)
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue
from calculations.domain.entities.person import Person
from infrastructure.database.repository.base import SqlBaseRepo
from libs.types.identifiers import ExpenseUUID, PersonUUID, RevenueUUID, UserUUID


class BalanceRepo(SqlBaseRepo, AbstractBalanceRepo):
    def __init__(self):
        super().__init__()
        self.expenses_to_save: Set[Expense] = set()
        self.revenues_to_save: Set[Revenue] = set()
        self.balance_to_save: Balance | None = None
        self.revenues_to_delete: Set[Revenue] = set()
        self.expenses_to_delete: Set[Expense] = set()

    def get_balance_by_month_year_and_person(
        self, month: int, year: int, person_id: PersonUUID
    ) -> Optional[Balance]:
        with self:
            query = select(Balance).where(
                Balance.month == month,
                Balance.year == year,
                Balance.person_id == person_id,
            )
            balance = self.session.execute(query).scalar_one_or_none()

        return balance

    def get_all_balances_from_year_and_person(
        self, year: int, person_id: PersonUUID
    ) -> Iterable[Balance]:
        with self:
            query = select(Balance).where(
                Balance.start_date >= date(year, 1, 1),
                Balance.end_date <= date(year, 12, 31),
                Balance.person_id == person_id,
            )
            balances = self.session.execute(query).scalars().all()

        return balances

    def get_balance_by_expense_id_and_person_id(
        self, expense_id: ExpenseUUID, person_id: PersonUUID
    ) -> Optional[Balance]:
        with self:
            query = select(Balance).where(
                Balance.expenses.any(Expense.expense_id == expense_id),
                Balance.person_id == person_id,
            )
            balance = self.session.execute(query).scalar_one_or_none()
        return balance

    def get_balance_by_revenue_id_and_person_id(
        self, revenue_id: RevenueUUID, person_id: PersonUUID
    ) -> Optional[Balance]:
        with self:
            query = select(Balance).where(
                Balance.revenues.any(Revenue.revenue_id == revenue_id),
                Balance.person_id == person_id,
            )
            balance = self.session.execute(query).scalar_one_or_none()
        return balance

    def get_expense_by_id(self, expense_id: str) -> Optional[Expense]:
        with self:
            query = select(Expense).where(Expense.expense_id == ExpenseUUID(expense_id))
            expense = self.session.execute(query).scalar_one_or_none()

        return expense

    def get_revenue_by_id(self, revenue_id: str) -> Optional[Revenue]:
        with self:
            query = select(Revenue).where(Revenue.revenue_id == RevenueUUID(revenue_id))
            revenue = self.session.execute(query).scalar_one_or_none()

        return revenue

    def get_person_by_user_id(self, user_id: UserUUID) -> Optional[Person]:
        with self:
            query = select(Person).where(Person.user_id == user_id)
            person = self.session.execute(query).scalar_one_or_none()
        return person

    def get_all_expenses_by_person_id(
        self, person_id: PersonUUID
    ) -> Optional[list[Expense]]:
        with self:
            query = (
                select(Expense)
                .where(Expense.person_id == person_id)
                .order_by(Expense.description.desc())
            )
            expenses = self.session.execute(query).scalars().all()
        return expenses

    def get_all_revenues_by_person_id(
        self, person_id: PersonUUID
    ) -> Optional[list[Revenue]]:
        with self:
            query = (
                select(Revenue)
                .where(Revenue.person_id == person_id)
                .order_by(Revenue.description.desc())
            )
            revenues = self.session.execute(query).scalars().all()
        return revenues

    def remove_expense(self, expense: Expense) -> None:
        self.expenses_to_delete.add(expense)

    def remove_revenue(self, revenue: Revenue) -> None:
        self.revenues_to_delete.add(revenue)

    def _add_or_update_expense(self) -> None:
        for expense_to_save in self.expenses_to_save:
            index = next(
                (
                    index
                    for index, expense in enumerate(self.balance_to_save.expenses)
                    if expense.expense_id == expense_to_save.expense_id
                ),
                None,
            )
            if index is not None:
                self.balance_to_save.expenses[index] = expense_to_save
            else:
                self.balance_to_save.expenses.append(expense_to_save)

    def save_balance(self, balance: Balance) -> None:
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
