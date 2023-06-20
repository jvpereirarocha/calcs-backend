from calculations.domain.abstractions.repository.balances.abstract_repo_balance import AbstractBalanceRepo
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue
from infrastructure.database.repository.base import SqlBaseRepo


class BalanceRepo(SqlBaseRepo, AbstractBalanceRepo):
    def __init__(self):
        self.objects_of_balance = set()

    def save_balance(self, balance: Balance) -> None:
        self.objects_of_balance.add(balance)
    
    def save_revenue(self, revenue: Revenue) -> None:
        with self:
            self.session.add(revenue)
    
    def save_expense(self, expense: Expense) -> None:
        with self:
            self.session.add(expense)

    def commit(self):
        list_of_objects = list(self.objects_of_balance)
        with self:
            self.session.bulk_save_objects(list_of_objects)
            self.session.commit()