"""add foreign key person_user

Revision ID: 3b8d0e0f6ba8
Revises: b52fe5e39b50
Create Date: 2022-08-29 23:43:58.042770

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "3b8d0e0f6ba8"
down_revision = "b52fe5e39b50"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("persons", Column("user_id", UUID, ForeignKey("users.id")))
    op.create_index("idx_person_user_id", "persons", ["user_id"])


def downgrade():
    op.drop_index("idx_person_user_id", table_name="persons", if_exists=True)
    op.drop_column("persons", "user_id")
