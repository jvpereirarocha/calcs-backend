from datetime import date, datetime, timedelta
from typing import List

from calculations.adapters.exceptions.date_hour import InvalidDateRange


class DateRange:
    def __init__(self, start: datetime, end: datetime) -> None:
        self.start = start
        self.end = self._get_last_hour_of_day(end=end)
        self._format = "%d/%m/%Y %H:%M:%S"

    def _get_last_hour_of_day(self, end: datetime) -> datetime:
        return datetime(
            year=end.year,
            month=end.month,
            day=end.day,
            hour=23,
            minute=59,
            second=59,
            microsecond=999_999
        )

    def __new__(cls, start: datetime, end: datetime):
        if start > end:
            raise InvalidDateRange("Invalid DateRange")
        
        return super().__new__(cls)

    def _get_correct_condition(self, start: datetime, end: datetime, consider_last_day: bool = True):
        if consider_last_day:
            return start <= end
        return start < end

    def get_dates_from_interval(self, consider_last_day: bool = True) -> List[date]:
        dates = []
        start = self.start
        end = self.end
        condition = self._get_correct_condition(start=start, end=end, consider_last_day=consider_last_day)
        while condition:
            current_date = date(year=start.year, month=start.month, day=start.day)
            yield current_date
            start = start + timedelta(days=1)

    def _texted_format_daterange(self):
        return f"<Start: {self.start.strftime(self._format)} - End: {self.end.strftime(self._format)}>"

    def __str__(self) -> str:
        return self._texted_format_daterange()
    
    def __repr__(self) -> str:
        return self._texted_format_daterange()