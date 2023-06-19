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
            ENUM(name="balance_status"),
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


def downgrade():
    op.drop_table("balances")
