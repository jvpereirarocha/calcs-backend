from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import PersonUUID, UserUUID


metadata_obj = MetaData()

persons = CustomTable(
    'user',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", UserUUID),
    CustomColumn('email', String(255)),
    CustomColumn('password', DateTime),
    CustomColumn('avatar', String(255), nullable=True),
)