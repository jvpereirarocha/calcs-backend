from abc import ABC, abstractmethod
from typing import Iterable, Optional
from calculations.domain.abstractions.repository.base.abstract_repo import AbstractRepo
from libs.types.identifiers import ExpenseUUID

from calculations.domain.entities.expenses import Expense


class AbstractRepoExpense(AbstractRepo):
    @abstractmethod
    def get_all_expenses(self) -> Iterable[Expense]:
        raise NotImplementedError()

    @abstractmethod
    def get_expense_by_id(self, expense_id: ExpenseUUID) -> Optional[Expense]:
        raise NotImplementedError()
