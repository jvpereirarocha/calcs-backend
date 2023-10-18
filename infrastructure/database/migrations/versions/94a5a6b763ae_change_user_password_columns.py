"""change user password columns

Revision ID: 94a5a6b763ae
Revises: 65c6e15ec8d9
Create Date: 2023-09-07 11:53:16.410397

"""
from alembic import op
from sqlalchemy import Column, LargeBinary, String
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "94a5a6b763ae"
down_revision = "65c6e15ec8d9"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "users",
        "password",
        nullable=False,
        new_column_name="password_hash",
        existing_type=String(255),
        type_=LargeBinary,
        postgresql_using="password::bytea",
    )
    op.add_column("users", Column("password_salt", LargeBinary, nullable=True))


def downgrade():
    op.alter_column(
        "users",
        "password_hash",
        nullable=False,
        new_column_name="password",
        type_=String(255),
    )
    op.drop_column("users", "password_salt")
