"""create balance foreign key

Revision ID: 65c6e15ec8d9
Revises: 3a587e2d171c
Create Date: 2023-05-16 18:43:18.909767

"""
from alembic import op
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '65c6e15ec8d9'
down_revision = '3a587e2d171c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'expenses',
        Column('balance_id', UUID, ForeignKey('balances.id'))
    )
    op.add_column(
        'revenues',
        Column('balance_id', UUID, ForeignKey('balances.id'))
    )


def downgrade():
    op.drop_column('expenses', 'balance_id')
    op.drop_column('revenues', 'balance_id')
