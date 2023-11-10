"""create balance foreign key

Revision ID: 65c6e15ec8d9
Revises: 3a587e2d171c
Create Date: 2023-05-16 18:43:18.909767

"""
from alembic import op
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "65c6e15ec8d9"
down_revision = "3a587e2d171c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("expenses", Column("balance_id", UUID, ForeignKey("balances.id")))
    op.add_column("revenues", Column("balance_id", UUID, ForeignKey("balances.id")))
    op.create_index("idx_expense_balance_id", "expenses", ["balance_id"])
    op.create_index("idx_revenue_balance_id", "revenues", ["balance_id"])


def downgrade():
    op.drop_index("idx_expense_balance_id", table_name="expenses", if_exists=True)
    op.drop_index("idx_revenue_balance_id", table_name="revenues", if_exists=True)
    op.drop_column("expenses", "balance_id")
    op.drop_column("revenues", "balance_id")
