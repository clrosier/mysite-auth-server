"""empty message

Revision ID: 16e36eec694a
Revises: 05840c478ced
Create Date: 2020-01-28 15:06:39.725307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16e36eec694a'
down_revision = '05840c478ced'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
