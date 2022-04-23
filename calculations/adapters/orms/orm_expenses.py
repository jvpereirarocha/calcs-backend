from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import ExpenseUUID


metadata_obj = MetaData()

expenses = CustomTable(
    'expense',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", ExpenseUUID),
    CustomColumn('description', String(255)),
    CustomColumn('value', Float(asdecimal=True)),
    CustomColumn('due_date', DateTime, default=datetime.utcnow),
    CustomColumn('already_paid', Boolean, default=False),
    CustomColumn('category', String(100), default='other'),
)