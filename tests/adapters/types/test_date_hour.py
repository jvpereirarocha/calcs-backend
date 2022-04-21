from datetime import datetime, timedelta

import pytest
from calculations.adapters.types.date_hour import DateRange
from calculations.adapters.exceptions.date_hour import InvalidDateRange


def test_date_range_when_is_valid():
    start = datetime.now()
    end = datetime.now() + timedelta(days=7)
    date_range = DateRange(start=start, end=end)
    assert isinstance(date_range, DateRange)


def test_invalid_date_range():
    start = datetime.now() + timedelta(days=20)
    end = datetime.now() + timedelta(days=5)
    with pytest.raises(InvalidDateRange):
        date_range = DateRange(start=start, end=end)