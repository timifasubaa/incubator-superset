"""csv_upload_destination

Revision ID: 5c4cb6c8145b
Revises: ca69c70ec99b
Create Date: 2017-08-28 11:09:39.385322

"""

# revision identifiers, used by Alembic.
revision = '5c4cb6c8145b'
down_revision = 'ca69c70ec99b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('dbs', sa.Column('csv_upload_destination', sa.String(length=250), nullable=True))


def downgrade():
    op.drop_column('dbs', 'csv_upload_destination')
