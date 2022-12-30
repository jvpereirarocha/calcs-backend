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
revision = '672acc87c093'
down_revision = 'db68742ce70e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'accounts',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('number_of_account', sa.String(50), nullable=False),
        sa.Column('amount', sa.String(255), nullable=False),
        sa.Column('person_id', UUID, sa.ForeignKey('persons.id')),
        sa.Column('created_when', sa.DateTime, default=func.now()),
        sa.Column('modified_when', sa.DateTime, default=func.now()),
    )


def downgrade():
    op.drop_table('accounts')
