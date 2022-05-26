"""remove likes count from Posts

Revision ID: 898b2dd46e51
Revises: 77a18a2095f2
Create Date: 2022-05-23 01:58:01.309307

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '898b2dd46e51'
down_revision = '77a18a2095f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('likes', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
