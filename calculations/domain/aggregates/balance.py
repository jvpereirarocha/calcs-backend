from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from datetime import date, datetime
from typing import List, Optional, Self
from libs.types.identifiers import BalanceUUID, ExpenseUUID, PersonUUID, RevenueUUID
from libs.types.date_hour import DateRange
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
    expenses: Optional[list[Expense]] = field(default_factory=list)
    revenues: Optional[list[Revenue]] = field(default_factory=list)
    person_id: Optional[PersonUUID] = None
    status_balance: StatusBalance = StatusBalance.INITIAL
    created_when: Optional[datetime] = None
    modified_when: Optional[datetime] = None

    def __hash__(self) -> int:
        return hash(self.balance_id)

    def __str__(self):
        return f"<Balance of {self.month}/{self.year}>"

    @property
    def sum_of_all_expenses_on_month(self) -> float:
        return sum([expense.value for expense in self.expenses])

    @property
    def sum_of_all_revenues_on_month(self) -> float:
        return sum([revenue.value for revenue in self.revenues])

    def calculate_total_of_balance(self) -> Decimal:
        value = Decimal(
            self.sum_of_all_revenues_on_month - self.sum_of_all_expenses_on_month
        )
        return round(value, 2)

    def calculate_total_of_expenses(self) -> Decimal:
        value = Decimal(sum((expense.value for expense in self.expenses), 0))
        return round(value, 2)

    def calculate_total_of_revenues(self) -> Decimal:
        value = Decimal(sum((revenue.value for revenue in self.revenues), 0))
        return round(value, 2)

    @property
    def month_balance(self) -> Decimal:
        return self.calculate_total_of_balance()

    @property
    def expenses_amount(self) -> Decimal:
        return self.calculate_total_of_expenses()

    @property
    def revenues_amount(self) -> Decimal:
        return self.calculate_total_of_revenues()

    @property
    def date_range(self):
        return DateRange(start=self.start_date, end=self.end_date)

    def get_expense_by_id(self, expense_id: ExpenseUUID) -> Optional[Expense]:
        return next(
            (expense for expense in self.expenses if expense.expense_id == expense_id),
            None,
        )

    def get_revenue_by_id(self, revenue_id: RevenueUUID) -> Optional[Revenue]:
        return next(
            (revenue for revenue in self.revenues if revenue.revenue_id == revenue_id),
            None,
        )

    def sum_balance_based_on_month_transactions(self) -> float:
        return (
            self.total_of_balance + self.sum_of_all_revenues
        ) - self.sum_of_all_expenses_on_month

    def balance_with_negative_value(self) -> bool:
        return self.sum_balance_based_on_month_transactions() < 0

    @classmethod
    def sum_all_balances_from_list_of_balances(cls, balances: List[Self]) -> Decimal:
        value = Decimal(
            sum((float(balance.month_balance) for balance in balances), 0.0)
        )
        return round(value, 2)

    @classmethod
    def sum_all_revenues_from_list_of_balances(cls, balances: List[Self]) -> Decimal:
        value = Decimal(
            sum((float(balance.revenues_amount) for balance in balances), 0.0)
        )
        return round(value, 2)

    @classmethod
    def sum_all_expenses_from_list_of_balances(cls, balances: List[Self]) -> Decimal:
        value = Decimal(
            sum((float(balance.expenses_amount) for balance in balances), 0.0)
        )
        return round(value, 2)
