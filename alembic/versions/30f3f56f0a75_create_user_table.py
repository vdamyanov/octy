"""create user table

Revision ID: 30f3f56f0a75
Revises: 
Create Date: 2015-05-10 20:43:49.642879

"""

# revision identifiers, used by Alembic.
revision = '30f3f56f0a75'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(120), nullable=False),
    )


def downgrade():
    op.drop_table('account')
