"""create accounts table

Revision ID: 672acc87c093
Revises: db68742ce70e
Create Date: 2022-12-30 00:40:18.521244

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = "672acc87c093"
down_revision = "db68742ce70e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "accounts",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("number_of_account", sa.String(50), nullable=False),
        sa.Column("amount", sa.Float, nullable=False),
        sa.Column("person_id", UUID, sa.ForeignKey("persons.id")),
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
    op.create_unique_constraint(
        "uq_account_number_of_account_person_id",
        "accounts",
        ["number_of_account", "person_id"],
    )
    op.create_index("idx_account_id", "accounts", ["id"])
    op.create_index("idx_account_number_of_account", "accounts", ["number_of_account"])
    op.create_index("idx_account_amount", "accounts", ["amount"])
    op.create_index("idx_account_person_id", "accounts", ["person_id"])


def downgrade():
    op.drop_index("idx_account_id", table_name="accounts", if_exists=True)
    op.drop_index(
        "idx_account_number_of_account", table_name="accounts", if_exists=True
    )
    op.drop_index("idx_account_amount", table_name="accounts", if_exists=True)
    op.drop_index("idx_account_person_id", table_name="accounts", if_exists=True)
    op.drop_constraint(
        "uq_account_number_of_account_person_id", "accounts", type_="unique"
    )
    op.drop_table("accounts")
