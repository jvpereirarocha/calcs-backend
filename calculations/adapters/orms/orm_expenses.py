from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import ExpenseUUID
from calculations.adapters.orms.orm_persons import persons
from calculations.adapters.orms.orm_accounts import accounts


metadata_obj = MetaData()

expenses = CustomTable(
    'expenses',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", ExpenseUUID),
    CustomColumn('description', String(255)),
    CustomColumn('value', Float(asdecimal=True)),
    CustomColumn('due_date', DateTime, default=datetime.utcnow),
    CustomColumn('already_paid', Boolean, default=False),
    CustomColumn('category', String(100), default='other'),
    CustomColumn('person_id', ForeignKey(persons.c.id, ondelete="CASCADE")),
)