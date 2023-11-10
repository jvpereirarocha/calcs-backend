"""create person id foreign key on balance table

Revision ID: 242cc6768c19
Revises: 94a5a6b763ae
Create Date: 2023-11-04 03:28:39.025378

"""
from alembic import op
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "242cc6768c19"
down_revision = "94a5a6b763ae"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("balances", Column("person_id", UUID, ForeignKey("persons.id")))
    op.create_unique_constraint(
        "uq_balance_month_year_person_id", "balances", ["month", "year", "person_id"]
    )
    op.create_index(
        "idx_balance_month_year_person_id", "balances", ["month", "year", "person_id"]
    )
    op.create_index("idx_balance_person_id", "balances", ["person_id"])


def downgrade():
    op.drop_index(
        "idx_balance_month_year_person_id", table_name="balances", if_exists=True
    )
    op.drop_index("idx_balance_person_id", "balances", if_exists=True)
    op.drop_constraint("uq_balance_month_year_person_id", "balances", type_="unique")
    op.drop_column("balances", "person_id")
