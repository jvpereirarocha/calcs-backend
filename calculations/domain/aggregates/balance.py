from dataclasses import dataclass
from typing import List, Optional
from calculations.adapters.types.basic_types import BalanceUUID
from calculations.adapters.types.date_hour import DateRange
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue


@dataclass
class Balance:
    id: BalanceUUID
    amount: float
    accounts: List[Account]
    person: Person
    month: int
    year: int
    date_range: DateRange
    expenses: Optional[List[Expense]]
    revenues: Optional[List[Revenue]]

    def __str__(self):
        return f"<Balance of {self.month}/{self.year} amount - R$: {self.amount}"

    def balance_with_negative_amount(self) -> bool:
        return True
