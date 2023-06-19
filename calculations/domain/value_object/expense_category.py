from enum import Enum


class ExpenseCategory(str, Enum):
    health: str = "health"
    food: str = "food"
    entertainment: str = "entertainment"
    transport: str = "transport"
    other: str = "other"
