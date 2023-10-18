from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from libs.types.identifiers import PersonUUID, RevenueUUID, BalanceUUID

from calculations.domain.entities.models import InheritedModel


@dataclass
class Revenue(InheritedModel):
    revenue_id: Optional[RevenueUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    date_of_receivment: Optional[datetime] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None
    balance_id: Optional[BalanceUUID] = None

    def __hash__(self) -> int:
        return hash(self.revenue_id)
