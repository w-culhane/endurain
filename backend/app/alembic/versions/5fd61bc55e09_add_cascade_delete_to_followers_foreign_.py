"""Add cascade delete to followers foreign keys

Revision ID: 5fd61bc55e09
Revises: 1bce2bd27873
Create Date: 2024-05-21 20:59:54.984566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fd61bc55e09'
down_revision: Union[str, None] = '1bce2bd27873'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('followers_ibfk_2', 'followers', type_='foreignkey')
    op.drop_constraint('followers_ibfk_1', 'followers', type_='foreignkey')
    op.create_foreign_key(None, 'followers', 'users', ['following_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'followers', 'users', ['follower_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.create_foreign_key('followers_ibfk_1', 'followers', 'users', ['follower_id'], ['id'])
    op.create_foreign_key('followers_ibfk_2', 'followers', 'users', ['following_id'], ['id'])
    # ### end Alembic commands ###