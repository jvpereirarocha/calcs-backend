from enum import Enum


class RevenueCategory(str, Enum):
    salary: str = "salary"
    investment: str = "investment"
    other: str = "other"
