"""add watch table

Revision ID: a013f2787086
Revises: 1a31ce608336
Create Date: 2024-08-05 20:21:10.912388

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'a013f2787086'
down_revision = '1a31ce608336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watch',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('brand', sqlmodel.sql.sqltypes.AutoString(length=32), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('colour', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_watch_brand'), 'watch', ['brand'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_watch_brand'), table_name='watch')
    op.drop_table('watch')
    # ### end Alembic commands ###
