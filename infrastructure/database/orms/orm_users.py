from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import CustomColumn, CustomTable
from libs.types.identifiers import UserUUID


metadata_obj = MetaData()

users = CustomTable(
    "users",
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", UserUUID),
    CustomColumn("email", String(255)),
    CustomColumn("password", String(255)),
    CustomColumn("avatar", String(255), nullable=True),
)
