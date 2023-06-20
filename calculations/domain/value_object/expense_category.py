from enum import StrEnum, auto


class ExpenseCategory(StrEnum):
    HEALTH: str = auto()
    FOOD: str = auto()
    ENTERTEINMENT: str = auto()
    TRANSPORT: str = auto()
    OTHER: str = auto()
