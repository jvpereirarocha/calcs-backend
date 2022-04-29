from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import AccountUUID
from calculations.adapters.orms.orm_persons import persons


metadata_obj = MetaData()

accounts = CustomTable(
    'account',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", AccountUUID),
    CustomColumn('number_of_account', String(255)),
    CustomColumn('value', Float(asdecimal=True)),
    CustomColumn('person_id', ForeignKey(persons.c.id, ondelete="CASCADE")),
)