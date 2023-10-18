from abc import ABC, abstractmethod

from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue


class AbstractBalanceRepo(AbstractRepo, ABC):
    @abstractmethod
    def save_balance(self, balance: Balance) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_revenue(self, revenue: Revenue) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_expense(self, expense: Expense) -> None:
        raise NotImplementedError()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()
