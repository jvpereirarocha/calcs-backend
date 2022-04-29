from dataclasses import dataclass

from calculations.adapters.types.basic_types import AccountUUID, PersonUUID
from calculations.domain.entities.models import BaseModel


@dataclass
class Account(BaseModel):
    id: AccountUUID
    number_of_account: str
    value: float
    person_id: PersonUUID