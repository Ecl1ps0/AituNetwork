"""add comments

Revision ID: c5aaa2a7ff68
Revises: c3a78793fa04
Create Date: 2022-06-01 10:52:49.228999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5aaa2a7ff68'
down_revision = 'c3a78793fa04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_user_id'), 'comments', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_user_id'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###