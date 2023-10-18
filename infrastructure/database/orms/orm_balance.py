from typing import List, TYPE_CHECKING
from sqlalchemy import Index, String, Float, Integer, DateTime, Date
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func
from sqlalchemy import UniqueConstraint
from infrastructure.database.orms.orm_base import (
    CustomColumn,
    CustomTable,
    metadata_base_obj,
)
from libs.types.identifiers import BalanceUUID
from calculations.domain.aggregates.balance import StatusBalance

if TYPE_CHECKING:
    from calculations.domain.entities.expenses import Expense


balances = CustomTable(
    "balances",
    metadata_base_obj,
    CustomColumn.UUID_as_primary_key("id", BalanceUUID),
    CustomColumn("description", String(255), nullable=False, default=""),
    CustomColumn("month", Integer, nullable=False),
    CustomColumn("year", Integer, nullable=False),
    CustomColumn("start_date", Date, nullable=False),
    CustomColumn("end_date", Date, nullable=False),
    CustomColumn("total_of_balance", Float(asdecimal=True)),
    CustomColumn(
        "status_balance",
        ENUM(
            StatusBalance.INITIAL.value,
            StatusBalance.ON_PROCESS.value,
            StatusBalance.FINISHED.value,
        ),
        nullable=False,
        default=StatusBalance.INITIAL.value,
    ),
    CustomColumn("created_when", DateTime, nullable=False, default=func.now()),
    CustomColumn("modified_when", DateTime, nullable=False, onupdate=func.now()),
    UniqueConstraint("month", "year", name="month_year_unique"),
    Index("idx_balance_id", "id"),
    Index("idx_balance_month_year", "month", "year"),
    Index("idx_balance_start_date_end_date", "start_date", "end_date"),
    Index("idx_balance_status", "status_balance"),
)
