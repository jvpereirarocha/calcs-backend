from dataclasses import dataclass

from calculations.adapters.types.basic_types import AccountUUID, PersonUUID
from calculations.domain.entities.models import BaseModel


@dataclass
class Account(BaseModel):
    account_id: AccountUUID
    number_of_account: str
    amount: float
    person_id: PersonUUID