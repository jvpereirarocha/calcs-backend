from datetime import datetime, timedelta
import pytest
import random
from typing import List, Optional
from libs.types.identifiers import BalanceUUID
from libs.types.date_hour import DateRange
from calculations.domain.aggregates.balance import Balance
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.person import Person
from calculations.domain.entities.revenues import Revenue


@pytest.fixture(scope="function")
def mock_balance_generate(mock_account, mock_person, mock_expense, mock_revenue):
    def make_mock(
        id: Optional[BalanceUUID] = None,
        value: Optional[float] = None,
        accounts: Optional[List[Account]] = None,
        person: Optional[Person] = None,
        month: Optional[int] = None,
        year: Optional[int] = None,
        date_range: Optional[DateRange] = None,
        expenses: Optional[List[Expense]] = None,
        revenues: Optional[List[Revenue]] = None,
    ):
        balance = Balance(
            balance_id=id or BalanceUUID(),
            value=value or random.uniform(0.0, 1000.0),
            accounts=accounts or [mock_account],
            person=person or mock_person,
            month=month or random.choice([i for i in range(1, 12)]),
            year=year or random.choice([i for i in range(2000, 2030)]),
            date_range=date_range
            or DateRange(start=datetime.now(), end=datetime.now() + timedelta(days=30)),
            expenses=expenses or [mock_expense],
            revenues=revenues or [mock_revenue],
        )

        return balance

    yield make_mock


@pytest.fixture(scope="function")
def mock_balance(mock_balance_generate):
    yield mock_balance_generate()
