from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import (
    CustomColumn,
    CustomTable,
    metadata_base_obj,
)
from libs.types.identifiers import ExpenseUUID
from infrastructure.database.orms.orm_persons import persons
from infrastructure.database.orms.orm_balance import balances


expenses = CustomTable(
    "expenses",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", ExpenseUUID),
    CustomColumn("description", String(255)),
    CustomColumn("value", Float(asdecimal=True)),
    CustomColumn("due_date", DateTime, default=datetime.utcnow),
    CustomColumn("already_paid", Boolean, default=False),
    CustomColumn("category", String(100), default="other"),
    CustomColumn("person_id", ForeignKey(persons.c.id, ondelete="CASCADE")),
    CustomColumn("balance_id", ForeignKey(balances.c.id, ondelete="CASCADE")),
)
