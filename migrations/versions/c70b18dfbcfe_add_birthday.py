"""add birthday

Revision ID: c70b18dfbcfe
Revises: 840efe6f6a5e
Create Date: 2022-06-01 04:20:26.606885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c70b18dfbcfe'
down_revision = '840efe6f6a5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('birthday', sa.DATETIME(), nullable=True))
    op.create_index(op.f('ix_users_birthday'), 'users', ['birthday'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_birthday'), table_name='users')
    op.drop_column('users', 'birthday')
    # ### end Alembic commands ###
