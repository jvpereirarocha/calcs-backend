from datetime import datetime
from sqlalchemy import Index
from sqlalchemy import UniqueConstraint
from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from infrastructure.database.orms.orm_base import (
    CustomColumn,
    CustomTable,
    metadata_base_obj,
)
from libs.types.identifiers import AccountUUID
from infrastructure.database.orms.orm_persons import persons


metadata_base_obj = MetaData()

accounts = CustomTable(
    "accounts",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", AccountUUID),
    CustomColumn("number_of_account", String(255)),
    CustomColumn("amount", Float(asdecimal=True)),
    CustomColumn("person_id", ForeignKey(persons.c.id, ondelete="CASCADE")),
    UniqueConstraint(
        "number_of_account", "person_id", name="uq_account_number_of_account_person_id"
    ),
    Index("idx_account_id", "id"),
    Index("idx_account_number_of_account", "number_of_account"),
    Index("idx_account_amount", "amount"),
    Index("idx_account_person_id", "person_id"),
)
