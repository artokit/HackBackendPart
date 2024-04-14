"""add lines in dots

Revision ID: a59218330753
Revises: 8ba829dbcebe
Create Date: 2024-04-13 00:41:22.783625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a59218330753'
down_revision: Union[str, None] = '8ba829dbcebe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dots', sa.Column('dots', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dots', 'dots')
    # ### end Alembic commands ###
