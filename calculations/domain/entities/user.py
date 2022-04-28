from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from calculations.adapters.types.basic_types import UserUUID


@dataclass
class User:
    id: UserUUID
    email: str
    password: str
    avatar: Optional[str] = None
