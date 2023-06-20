from typing import Set

from calculations.domain.abstractions.repository.balances.abstract_repo_balance import (
    AbstractBalanceRepo
)
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue


class FakeBalanceRepo(AbstractBalanceRepo):
    def __init__(self, data: Set[Balance | Expense | Revenue]):
        self.data = data
        self._list_of_objects = []
        self._commited = False

    @property
    def commited(self):
        return self._commited
    
    def save_expense(self, expense: Expense) -> None:
        self._list_of_objects.append(expense)
    
    def save_revenue(self, revenue: Revenue) -> None:
        self._list_of_objects.append(revenue)
    
    def save_balance(self, balance: Balance) -> None:
        self._list_of_objects.append(balance)

    def commit(self):
        for obj in self._list_of_objects:
            self.data.add(obj)

        self._commited = True
