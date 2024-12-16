"""Remove photo_path_aux column from users table

Revision ID: ab815ee3beae
Revises: 0ab200a7f196
Create Date: 2024-06-07 21:40:28.789274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ab815ee3beae'
down_revision: Union[str, None] = '0ab200a7f196'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'photo_path_aux')

    # Update admin password
    new_password = '$2b$12$.b.fWl/Bu/sIx/6ZtIgJPuXaqfqkIi8NwnxeP6SQiQPZB3kKxD5tm'
    op.execute(
        sa.text(
            """
            UPDATE users
            SET password = :new_password
            WHERE username = 'admin'
            """
        ).bindparams(new_password=new_password)
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('photo_path_aux', sa.VARCHAR(length=250), nullable=True, comment='Auxiliary photo path'))

    old_password = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    op.execute(
        sa.text(
            """
            UPDATE users
            SET password = :old_password
            WHERE username = 'admin'
            """
        ).bindparams(old_password=old_password)
    )

    # ### end Alembic commands ###
