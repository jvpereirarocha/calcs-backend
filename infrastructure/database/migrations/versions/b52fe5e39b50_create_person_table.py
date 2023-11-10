"""create person table

Revision ID: b52fe5e39b50
Revises: 2c275fd0b6e2
Create Date: 2022-08-29 23:31:16.087238

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "b52fe5e39b50"
down_revision = "2c275fd0b6e2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "persons",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("first_name", sa.String(255), nullable=False),
        sa.Column("last_name", sa.String(255), nullable=False),
        sa.Column("date_of_birth", sa.DateTime, nullable=False),
    )
    op.create_index("idx_person_id", "persons", ["id"])
    op.create_index("idx_person_first_name", "persons", ["first_name"])
    op.create_index("idx_person_last_name", "persons", ["last_name"])
    op.create_index("idx_person_date_of_birth", "persons", ["date_of_birth"])
    op.create_index(
        "idx_person_first_name_last_name", "persons", ["first_name", "last_name"]
    )


def downgrade():
    op.drop_table("persons")
