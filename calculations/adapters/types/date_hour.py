from datetime import datetime

from calculations.adapters.exceptions.date_hour import InvalidDateRange


class DateRange:
    def __init__(self, start: datetime, end: datetime) -> None:
        self.start = start
        self.end = end
        self._format = "%d/%m/%Y %H:%M:%S"

    def __new__(cls, start: datetime, end: datetime):
        if start > end:
            raise InvalidDateRange()
        
        return super().__new__(cls)

    def __str__(self) -> str:
        return f"<Start: {self.start.strftime(self._format)} - End: {self.end.strftime(self._format)}>"