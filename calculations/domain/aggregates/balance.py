from dataclasses import dataclass, field
from enum import Enum
from datetime import date, datetime
from typing import List, Optional
from calculations.adapters.types.basic_types import BalanceUUID
from calculations.adapters.types.date_hour import DateRange
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.revenues import Revenue


class StatusBalance(Enum):
    INITIAL = "initial"
    ON_PROCESS = "on process"
    FINISHED = "finished"


@dataclass
class Balance:
    balance_id: BalanceUUID
    description: str
    month: int
    year: int
    start_date: date
    end_date: date
    total_of_balance: float
    expenses: Optional[List[Expense]] = field(default_factory=list)
    revenues: Optional[List[Revenue]] = field(default_factory=list)
    status_balance: str = StatusBalance.INITIAL.value
    created_when: Optional[datetime] = None
    modified_when: Optional[datetime] = None

    def __str__(self):
        return f"<Balance of {self.month}/{self.year} amount - R$: {self.value}"

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
        return (self.total_of_balance + self.sum_of_all_revenues) - self.sum_of_all_expenses_on_month

    def balance_with_negative_value(self) -> bool:
        return self.sum_balance_based_on_month_transactions() < 0
