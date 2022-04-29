from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import PersonUUID
from calculations.adapters.orms.orm_users import users


metadata_obj = MetaData()

persons = CustomTable(
    'person',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", PersonUUID),
    CustomColumn('name', String(255)),
    CustomColumn('date_of_birth', DateTime),
    CustomColumn('user_id', ForeignKey(users.c.id, ondelete="CASCADE")),
)