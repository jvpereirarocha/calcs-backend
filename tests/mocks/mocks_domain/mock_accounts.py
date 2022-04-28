import pytest
import random
from typing import Optional
from calculations.adapters.types.basic_types import AccountUUID
from calculations.domain.entities.accounts import Account

@pytest.fixture(scope="function")
def mock_account_generate():

    def make_mock(
        id: Optional[AccountUUID] = None,
        number_of_account: Optional[str] = None,
        amount_on_account: Optional[float] = None
    ):
        account = Account(
            id=id or AccountUUID(),
            number_of_account=number_of_account or random.choice([str(i) * 5 for i in range(0, 9)]),
            amount_on_account=amount_on_account or random.uniform(0.0, 100.0),
        )

        return account

    yield make_mock


@pytest.fixture(scope="function")
def mock_account(mock_account_generate):
    yield mock_account_generate()