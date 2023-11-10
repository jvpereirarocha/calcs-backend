from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional
from libs.types.identifiers import PersonUUID, RevenueUUID, BalanceUUID

from calculations.domain.entities.models import InheritedModel
from calculations.domain.value_object.format import format_to_value


@dataclass
class Revenue(InheritedModel):
    revenue_id: Optional[RevenueUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    date_of_receivment: Optional[date] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None
    balance_id: Optional[BalanceUUID] = None

    def __hash__(self) -> int:
        return hash(self.revenue_id)

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "value": format_to_value(value=self.value),
            "category": self.category,
        }
