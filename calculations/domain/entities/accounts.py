from dataclasses import dataclass

from libs.types.identifiers import AccountUUID, PersonUUID
from calculations.domain.entities.models import InheritedModel


@dataclass
class Account(InheritedModel):
    account_id: AccountUUID
    number_of_account: str
    amount: float
    person_id: PersonUUID
