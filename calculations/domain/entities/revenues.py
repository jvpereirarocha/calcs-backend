from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Self, Union
from libs.types.identifiers import PersonUUID, RevenueUUID, BalanceUUID

from calculations.domain.entities.models import InheritedModel
from calculations.domain.value_object.format import format_to_value


RevenueType = Union[str, float, datetime, bool]


@dataclass
class Revenue(InheritedModel):
    revenue_id: Optional[RevenueUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    date_of_receivment: Optional[date] = None
    person_id: Optional[PersonUUID] = None
    category: Optional[str] = None
    balance_id: Optional[BalanceUUID] = None

    def __hash__(self) -> int:
        return hash(self.revenue_id)

    def check_if_attribute_was_updated_and_return_the_most_recent(
        self, old_value: RevenueType, new_value: RevenueType
    ) -> RevenueType:
        if new_value:
            return new_value
        return old_value

    def update_revenue(
        self,
        description: Optional[str] = None,
        value: Optional[float] = None,
        date_of_receivment: Optional[datetime] = None,
        category: Optional[str] = None,
    ) -> Self:
        self.description = (
            self.check_if_attribute_was_updated_and_return_the_most_recent(
                old_value=self.description, new_value=description
            )
        )
        self.value = self.check_if_attribute_was_updated_and_return_the_most_recent(
            old_value=self.value, new_value=value
        )
        self.date_of_receivment = (
            self.check_if_attribute_was_updated_and_return_the_most_recent(
                old_value=self.date_of_receivment, new_value=date_of_receivment
            )
        )
        self.category = self.check_if_attribute_was_updated_and_return_the_most_recent(
            old_value=self.category, new_value=category
        )
        self.modified_when = datetime.now()
        return self

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "value": format_to_value(value=self.value),
            "category": self.category,
        }
