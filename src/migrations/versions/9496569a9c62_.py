"""empty message

Revision ID: 9496569a9c62
Revises: 
Create Date: 2022-10-06 16:08:04.998451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9496569a9c62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('calls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lab', sa.Integer(), nullable=False),
    sa.Column('comp', sa.Integer(), nullable=False),
    sa.Column('problem', sa.String(length=60), nullable=False),
    sa.Column('description', sa.String(length=400), nullable=False),
    sa.Column('status', sa.String(length=60), nullable=False),
    sa.Column('time_created', sa.Date(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calls')
    op.drop_table('users')
    # ### end Alembic commands ###
