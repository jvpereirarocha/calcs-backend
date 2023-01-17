from sqlalchemy import String, Float, Integer, DateTime, Date
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func
from calculations.adapters.orms.orm_base import CustomColumn, CustomTable
from calculations.adapters.types.basic_types import BalanceUUID
from calculations.domain.aggregates.balance import StatusBalance


metadata_obj = MetaData()

balances = CustomTable(
    'balances',
    metadata_obj,
    CustomColumn.UUID_as_primary_key("id", BalanceUUID),
    CustomColumn('description', String(255), nullable=False, default=''),
    CustomColumn('month', Integer, nullable=False),
    CustomColumn('year', Integer, nullable=False),
    CustomColumn('start_date', Date, nullable=False),
    CustomColumn('end_date', Date, nullable=False),
    CustomColumn('total_of_balance', Float(asdecimal=True)),
    CustomColumn('status', ENUM, nullable=False, default=StatusBalance.INITIAL.value),
    CustomColumn('created_when', DateTime, nullable=False, default=func.now()),
    CustomColumn('modified_when', DateTime, nullable=False, onupdate=func.now()),
)