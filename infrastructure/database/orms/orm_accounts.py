from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import CustomColumn, CustomTable
from libs.types.identifiers import AccountUUID
from infrastructure.database.orms.orm_persons import persons


metadata_obj = MetaData()

accounts = CustomTable(
    "accounts",
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", AccountUUID),
    CustomColumn("number_of_account", String(255)),
    CustomColumn("amount", Float(asdecimal=True)),
    CustomColumn("person_id", ForeignKey(persons.c.id, ondelete="CASCADE")),
)
