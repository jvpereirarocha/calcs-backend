from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy import LargeBinary
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import (
    CustomColumn,
    CustomTable,
    metadata_base_obj,
)
from libs.types.identifiers import UserUUID


users = CustomTable(
    "users",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", UserUUID),
    CustomColumn("email", String(255)),
    CustomColumn("password_hash", LargeBinary(60)),
    CustomColumn("password_salt", LargeBinary(29)),
    CustomColumn("avatar", String(255), nullable=True),
    Index("idx_user_id", "id"),
    Index("idx_user_email", "email"),
    Index("idx_user_avatar", "avatar"),
    Index("idx_user_email_avatar", "email", "avatar"),
)
