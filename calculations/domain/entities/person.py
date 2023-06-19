from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from libs.types.identifiers import UserUUID, PersonUUID
from calculations.domain.entities.accounts import Account
from calculations.domain.entities.expenses import Expense
from calculations.domain.entities.models import InheritedModel
from calculations.domain.entities.revenues import Revenue


@dataclass
class Person(InheritedModel):
    person_id: PersonUUID
    first_name: str
    last_name: str
    date_of_birth: datetime
    accounts: Optional[List[Account]] = field(default_factory=list)
    expenses: Optional[List[Expense]] = field(default_factory=list)
    revenues: Optional[List[Revenue]] = field(default_factory=list)
    user_id: Optional[UserUUID] = None

    def __hash__(self) -> int:
        return id(self.person_id)

    @classmethod
    def create_person(
        cls,
        person_id: PersonUUID,
        first_name: str,
        last_name: str,
        date_of_birth: datetime,
        user_id: Optional[UserUUID] = None,
    ) -> "Person":
        return cls(
            person_id=person_id,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            user_id=user_id,
            created_when=datetime.now(),
            modified_when=datetime.now(),
        )

    def update_person(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        date_of_birth: Optional[datetime] = None,
    ) -> None:
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if date_of_birth:
            self.date_of_birth = date_of_birth

        self.modified_when = datetime.now()

    def to_dict(self):
        return {
            "person_id": str(self.person_id),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name),
            "date_of_birth": datetime.strftime(self.date_of_birth, "%d/%m/%Y"),
        }
