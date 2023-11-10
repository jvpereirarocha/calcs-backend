"""create expenses table

Revision ID: 98a77322a18c
Revises: d6ce6aa3e6f9
Create Date: 2022-12-30 01:04:46.047123

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = "98a77322a18c"
down_revision = "d6ce6aa3e6f9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "expenses",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("value", sa.Float, nullable=False),
        sa.Column("due_date", sa.Date, nullable=True),
        sa.Column("already_paid", sa.Boolean, nullable=False, default=False),
        sa.Column("person_id", UUID, sa.ForeignKey("persons.id")),
        sa.Column("category", sa.String(100), default="other"),
        sa.Column(
            "created_when",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "modified_when",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now(),
        ),
    )
    op.create_index("idx_expense_id", "expenses", ["id"])
    op.create_index("idx_expense_description", "expenses", ["description"])
    op.create_index("idx_expense_value", "expenses", ["value"])
    op.create_index("idx_expense_due_date", "expenses", ["due_date"])
    op.create_index("idx_expense_already_paid", "expenses", ["already_paid"])
    op.create_index("idx_expense_category", "expenses", ["category"])
    op.create_index("idx_expense_person_id", "expenses", ["person_id"])
    op.create_index(
        "idx_expense_description_value", "expenses", ["description", "value"]
    )


def downgrade():
    op.drop_index("idx_expense_id", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_description", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_value", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_due_date", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_already_paid", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_category", table_name="expenses", if_exists=True)
    op.drop_index("idx_expense_person_id", table_name="expenses", if_exists=True)
    op.drop_index(
        "idx_expense_description_value", table_name="expenses", if_exists=True
    )
    op.drop_table("expenses")
