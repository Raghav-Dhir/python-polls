"""create_polls_table

Revision ID: 5abe83febb76
Revises: cbaa3edc2583
Create Date: 2023-02-06 18:34:36.089795

"""
import enum
from alembic import op
import sqlalchemy as sa

pg = sa.dialects.postgresql

class PollType(enum.Enum):
    text=1
    image=2

# revision identifiers, used by Alembic.
revision = '5abe83febb76'
down_revision = 'cbaa3edc2583'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(250), nullable=False),
        sa.Column('type', pg.ENUM(PollType, create_type=False), nullable = False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable = False),
        sa.Column('is_voting_active', sa.Boolean, nullable = False),
        sa.Column('created_by', sa.Integer, nullable = False),
        sa.Column('created_at', sa.DateTime, nullable = False),
        sa.Column('updated_at', sa.DateTime, nullable = False)
    )


def downgrade():
    op.drop_table('polls')
