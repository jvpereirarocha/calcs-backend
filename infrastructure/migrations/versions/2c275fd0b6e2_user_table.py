"""user table

Revision ID: 2c275fd0b6e2
Revises: 
Create Date: 2022-05-04 22:22:07.444588

"""
import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '2c275fd0b6e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(32), nullable=False),
        sa.Column('avatar', sa.String(255), nullable=True),
    )


def downgrade():
    op.drop_table('users')
