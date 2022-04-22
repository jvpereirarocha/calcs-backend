from dataclasses import dataclass

from calculations.adapters.types.basic_types import AccountUUID, BalanceUUID, PersonUUID


@dataclass
class Account:
    id: AccountUUID
    number_of_account: str
    amount_on_account: float
    person_id: PersonUUID
    balance_id: BalanceUUID