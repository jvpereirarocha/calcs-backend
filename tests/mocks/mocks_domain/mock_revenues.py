from datetime import datetime
import pytest
import random
from typing import Optional
from libs.types.identifiers import RevenueUUID
from calculations.domain.entities.revenues import Revenue
from calculations.domain.value_object.revenue_category import RevenueCategory

@pytest.fixture(scope="function")
def mock_revenue_generate(mock_account):

    def make_mock(
        id: Optional[RevenueUUID] = None,
        description: Optional[str] = None,
        value: Optional[float] = None,
        date_of_receivment: Optional[datetime] = None,
        modified_when: Optional[datetime] = None
    ):
        revenue = Revenue(
            revenue_id=id or RevenueUUID(),
            description=description or random.choice(["revenue 1", "revenue 2", "revenue 3"]),
            value=value or random.uniform(1.0, 100.0),
            date_of_receivment=date_of_receivment or datetime.now(),
            account_of_receivment=mock_account,
            category=random.choice([RevenueCategory.salary, RevenueCategory.investment, RevenueCategory.other]),
            created_when=datetime.now(),
            modified_when=modified_when or datetime.now(),
        )

        return revenue

    yield make_mock


@pytest.fixture(scope="function")
def mock_revenue(mock_revenue_generate):
    yield mock_revenue_generate()