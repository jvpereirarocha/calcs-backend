from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from calculations.adapters.types.basic_types import BalanceUUID, PersonUUID
from calculations.adapters.types.date_hour import DateRange
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue


@dataclass
class Balance:
    balance_id: BalanceUUID
    month: int
    year: int
    start_date: datetime
    end_date: datetime
    value: float
    accounts: Optional[List[Account]] = field(default_factory=list)
    expenses: Optional[List[Expense]] = field(default_factory=list)
    revenues: Optional[List[Revenue]] = field(default_factory=list)

    def __str__(self):
        return f"<Balance of {self.month}/{self.year} amount - R$: {self.value}"

    @property
    def sum_account_values(self):
        return sum([account.amount for account in self.accounts])

    @property
    def sum_of_all_expenses_on_month(self) -> float:
        return sum([expense.value for expense in self.expenses])

    @property
    def sum_of_all_revenues(self) -> float:
        return sum([revenue.value for revenue in self.revenues])

    @property
    def date_range(self):
        return DateRange(start=self.start_date, end=self.end_date)

    def sum_balance_based_on_month_transactions(self) -> float:
        return (self.sum_account_values + self.sum_of_all_revenues) - self.sum_of_all_expenses_on_month

    def balance_with_negative_value(self) -> bool:
        return self.sum_balance_based_on_month_transactions() < 0
