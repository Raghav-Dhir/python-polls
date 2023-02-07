"""create_user_table

Revision ID: cbaa3edc2583
Revises: 
Create Date: 2023-02-06 17:30:31.989120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbaa3edc2583'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(30), nullable=False),
        sa.Column('email', sa.String(50), nullable = False),
        sa.Column('created_at', sa.DateTime, nullable = True),
        sa.Column('updated_at', sa.DateTime, nullable = True)
    )


def downgrade():
    op.drop_table('users')
