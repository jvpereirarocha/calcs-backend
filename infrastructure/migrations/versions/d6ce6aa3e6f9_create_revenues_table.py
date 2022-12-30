"""create revenues table

Revision ID: d6ce6aa3e6f9
Revises: 672acc87c093
Create Date: 2022-12-30 00:55:36.337447

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = 'd6ce6aa3e6f9'
down_revision = '672acc87c093'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'revenues',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('value', sa.Float, nullable=False),
        sa.Column('date_of_receivment', sa.DateTime, nullable=True),
        sa.Column('person_id', UUID, sa.ForeignKey('persons.id')),
        sa.Column('category', sa.String(100), default="other"),
        sa.Column('created_when', sa.DateTime, nullable=False, default=func.now()),
        sa.Column('modified_when', sa.DateTime, nullable=False, default=func.now()),
    )


def downgrade():
    op.drop_table('revenues')