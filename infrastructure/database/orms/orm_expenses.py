from datetime import datetime, date
from sqlalchemy import Boolean
from sqlalchemy import DateTime, Date
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import Index
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
    CustomColumn("due_date", Date, nullable=True),
    CustomColumn("already_paid", Boolean, default=False),
    CustomColumn("category", String(100), default="other"),
    CustomColumn("person_id", ForeignKey(persons.c.id, ondelete="CASCADE")),
    CustomColumn("balance_id", ForeignKey(balances.c.id, ondelete="CASCADE")),
    Index("idx_expense_id", "id"),
    Index("idx_expense_description", "description"),
    Index("idx_expense_value", "value"),
    Index("idx_expense_due_date", "due_date"),
    Index("idx_expense_already_paid", "already_paid"),
    Index("idx_expense_category", "category"),
    Index("idx_expense_person_id", "person_id"),
    Index("idx_expense_balance_id", "balance_id"),
    Index("idx_expense_description_value", "description", "value"),
)
