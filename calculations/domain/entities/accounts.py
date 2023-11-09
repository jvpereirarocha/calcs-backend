from dataclasses import dataclass
from typing import Optional

from libs.types.identifiers import AccountUUID, PersonUUID
from calculations.domain.entities.models import InheritedModel


@dataclass
class Account(InheritedModel):
    account_id: Optional[AccountUUID] = None
    number_of_account: Optional[str] = ""
    amount: Optional[float] = 0.0
