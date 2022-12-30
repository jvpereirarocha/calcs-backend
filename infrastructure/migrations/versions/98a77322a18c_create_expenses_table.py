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
revision = '98a77322a18c'
down_revision = 'd6ce6aa3e6f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'expenses',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('value', sa.Float, nullable=False),
        sa.Column('due_date', sa.DateTime, nullable=True),
        sa.Column('already_paid', sa.Boolean, nullable=False, default=False),
        sa.Column('person_id', UUID, sa.ForeignKey('persons.id')),
        sa.Column('category', sa.String(100), default="other"),
        sa.Column('created_when', sa.DateTime, nullable=False, default=func.now()),
        sa.Column('modified_when', sa.DateTime, nullable=False, default=func.now()),
    )


def downgrade():
    op.drop_table('expenses')
