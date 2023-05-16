from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import CustomColumn, CustomTable
from libs.types.identifiers import RevenueUUID
from infrastructure.database.orms.orm_persons import persons
from infrastructure.database.orms.orm_balance import balances


metadata_obj = MetaData()

revenues = CustomTable(
    'revenues',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", RevenueUUID),
    CustomColumn('description', String(255)),
    CustomColumn('value', Float(asdecimal=True)),
    CustomColumn('date_of_receivment', DateTime, default=datetime.utcnow),
    CustomColumn('category', String(100), default='other'),
    CustomColumn('person_id', ForeignKey(persons.c.id, ondelete="CASCADE")),
    CustomColumn('balance_id', ForeignKey(balances.c.id, ondelete="CASCADE")),
)