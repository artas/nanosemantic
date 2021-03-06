"""empty message

Revision ID: f5322d61330f
Revises: 
Create Date: 2021-12-11 07:09:05.927320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5322d61330f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('car_type', sa.String(), nullable=False),
    sa.Column('year_publication', sa.Date(), nullable=False),
    sa.Column('mark', sa.String(), nullable=False),
    sa.Column('mileage', sa.Integer(), nullable=False),
    sa.Column('horsepower', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###
