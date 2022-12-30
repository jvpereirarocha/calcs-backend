from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from calculations.adapters.types.basic_types import UserUUID
from calculations.domain.entities.models import BaseModel


@dataclass
class User(BaseModel):
    user_id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None
