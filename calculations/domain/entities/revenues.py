from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from calculations.adapters.types.basic_types import PersonUUID, RevenueUUID

from calculations.domain.entities.models import BaseModel


@dataclass
class Revenue(BaseModel):
    revenue_id: Optional[RevenueUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    date_of_receivment: Optional[datetime] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None