"""add created and modified when

Revision ID: db68742ce70e
Revises: 3b8d0e0f6ba8
Create Date: 2022-08-29 23:52:58.449298

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, func


# revision identifiers, used by Alembic.
revision = 'db68742ce70e'
down_revision = '3b8d0e0f6ba8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',
        Column('created_when', sa.DateTime, default=func.now()),
    )
    op.add_column('users',
        Column('modified_when', sa.DateTime, default=func.now()),
    )
    op.add_column('persons',
        Column('created_when', sa.DateTime, default=func.now()),
    )
    op.add_column('persons',
        Column('modified_when', sa.DateTime, default=func.now()),
    )


def downgrade():
    op.drop_column('users', 'created_when')
    op.drop_column('users', 'modified_when')
    op.drop_column('persons', 'created_when')
    op.drop_column('persons', 'modified_when')
