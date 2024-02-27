"""implement relationships

Revision ID: d4081dfc2582
Revises: 27042eb8f8c0
Create Date: 2024-02-27 10:05:34.035202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4081dfc2582'
down_revision = '27042eb8f8c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('missions', sa.Column('planet_id', sa.Integer(), nullable=True))
    op.add_column('missions', sa.Column('scientist_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_missions_scientist_id_scientists'), 'missions', 'scientists', ['scientist_id'], ['id'])
    op.create_foreign_key(op.f('fk_missions_planet_id_planets'), 'missions', 'planets', ['planet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_missions_planet_id_planets'), 'missions', type_='foreignkey')
    op.drop_constraint(op.f('fk_missions_scientist_id_scientists'), 'missions', type_='foreignkey')
    op.drop_column('missions', 'scientist_id')
    op.drop_column('missions', 'planet_id')
    # ### end Alembic commands ###
