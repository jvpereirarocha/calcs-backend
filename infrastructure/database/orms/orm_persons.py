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
from libs.types.identifiers import PersonUUID
from infrastructure.database.orms.orm_users import users


persons = CustomTable(
    "persons",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", PersonUUID),
    CustomColumn("first_name", String(255)),
    CustomColumn("last_name", String(255)),
    CustomColumn("date_of_birth", DateTime),
    CustomColumn("user_id", ForeignKey(users.c.id, ondelete="CASCADE")),
)
