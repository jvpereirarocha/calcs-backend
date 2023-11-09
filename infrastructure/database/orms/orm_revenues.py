from sqlalchemy import Date
from sqlalchemy import Index
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from infrastructure.database.orms.orm_base import (
    CustomColumn,
    CustomTable,
    metadata_base_obj,
)
from libs.types.identifiers import RevenueUUID
from infrastructure.database.orms.orm_persons import persons
from infrastructure.database.orms.orm_balance import balances


revenues = CustomTable(
    "revenues",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", RevenueUUID),
    CustomColumn("description", String(255)),
    CustomColumn("value", Float(asdecimal=True)),
    CustomColumn("date_of_receivment", Date, nullable=False),
    CustomColumn("category", String(100), default="other"),
    CustomColumn("person_id", ForeignKey(persons.c.id, ondelete="CASCADE")),
    CustomColumn("balance_id", ForeignKey(balances.c.id, ondelete="CASCADE")),
    Index("idx_revenue_id", "id"),
    Index("idx_revenue_description", "description"),
    Index("idx_revenue_value", "value"),
    Index("idx_revenue_date_of_receivment", "date_of_receivment"),
    Index("idx_revenue_category", "category"),
    Index("idx_revenue_person_id", "person_id"),
    Index("idx_revenue_balance_id", "balance_id"),
    Index("idx_revenue_description_value", "description", "value"),
)
