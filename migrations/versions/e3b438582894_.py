"""empty message

Revision ID: e3b438582894
Revises: 3d1c61a096ee
Create Date: 2022-05-05 01:11:00.317302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3b438582894'
down_revision = '3d1c61a096ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=30), nullable=True))
    # ### end Alembic commands ###
