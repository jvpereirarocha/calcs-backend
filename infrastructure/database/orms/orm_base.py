from datetime import datetime
from email.policy import default
from typing import Optional, Type
import uuid
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import func, util
from sqlalchemy import types
from sqlalchemy.dialects.postgresql import UUID


class CustomUUID(types.UserDefinedType):
    cache_ok = True
    __visit_name__ = "UUID"

    def __init__(self, class_type: Optional[Type[uuid.UUID]]) -> None:
        if class_type:
            self.class_type = class_type
        else:
            self.class_type = uuid.UUID

        self.as_uuid = True

    def bind_processor(self, dialect):
        def process(value):
            if value is not None:
                return value

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is not None:
                value = self.class_type(str(value))
            return value

        return process


class CustomColumn(Column):
    def __init__(self, *args, **kwargs) -> None:
        if "nullable" not in kwargs:
            kwargs["nullable"] = False

        super().__init__(*args, **kwargs)

    @staticmethod
    def UUID_as_primary_key(field_name: str, class_type=None):
        return Column(
            field_name,
            CustomUUID(class_type=class_type),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        )


class CustomTable(Table):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _init(cls, *args, **kwargs):
        super()._init(
            *args,
            CustomColumn(
                "created_when", DateTime(timezone=True), server_default=func.now()
            ),
            CustomColumn(
                "modified_when",
                DateTime(timezone=True),
                server_default=func.now(),
                server_onupdate=func.now(),
            ),
            **kwargs
        )
