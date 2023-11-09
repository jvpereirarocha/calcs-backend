from datetime import datetime
from sqlalchemy import Index
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
    Index("idx_person_id", "id"),
    Index("idx_person_first_name", "first_name"),
    Index("idx_person_last_name", "last_name"),
    Index("idx_person_date_of_birth", "date_of_birth"),
    Index("idx_person_user_id", "user_id"),
    Index("idx_person_first_name_last_name", "first_name", "last_name"),
)
