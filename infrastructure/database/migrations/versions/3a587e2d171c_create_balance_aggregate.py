"""create balance aggregate

Revision ID: 3a587e2d171c
Revises: 98a77322a18c
Create Date: 2023-01-16 23:55:50.777265

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = "3a587e2d171c"
down_revision = "98a77322a18c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "balances",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("description", sa.String(255), nullable=False, default=""),
        sa.Column("month", sa.Integer, nullable=False),
        sa.Column("year", sa.Integer, nullable=False),
        sa.Column(
            "total_of_balance", sa.Float(asdecimal=True), nullable=False, default=0.0
        ),
        sa.Column("start_date", sa.Date, nullable=False),
        sa.Column("end_date", sa.Date, nullable=False),
        sa.Column(
            "status_balance",
            ENUM("initial", "on_process", "finished", name="balance_status"),
            nullable=False,
            default="initial",
        ),
        sa.Column(
            "created_when", sa.DateTime(timezone=True), server_default=func.now()
        ),
        sa.Column(
            "modified_when",
            sa.DateTime(timezone=True),
            server_default=func.now(),
            server_onupdate=func.now(),
        ),
    )
    op.create_index("idx_balance_id", "balances", ["id"])
    op.create_index("idx_balance_description", "balances", ["description"])
    op.create_index("idx_balance_month", "balances", ["month"])
    op.create_index("idx_balance_year", "balances", ["year"])
    op.create_index("idx_balance_month_year", "balances", ["month", "year"])
    op.create_index("idx_balance_start_date_end_date", "balances", ["start_date", "end_date"])
    op.create_index("idx_balance_total_of_balance", "balances", ["total_of_balance"])
    op.create_index("idx_balance_status_balance", "balances", ["status_balance"])


def downgrade():
    op.drop_index("idx_balance_id", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_description", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_month", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_year", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_month_year", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_start_date_end_date", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_total_of_balance", table_name="balances", if_exists=True)
    op.drop_index("idx_balance_status_balance", table_name="balances", if_exists=True)
    op.drop_table("balances")
    op.execute("DROP TYPE balance_status;")
