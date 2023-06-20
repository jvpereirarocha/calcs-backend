from enum import StrEnum, auto


class RevenueCategory(StrEnum):
    SALARY: str = auto()
    INVESTMENT: str = auto()
    OTHER: str = auto()
