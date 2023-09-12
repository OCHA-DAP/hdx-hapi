"""create views

Revision ID: 5ea413542a49
Revises: be60e42db4db
Create Date: 2023-09-07 20:31:02.198042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ea413542a49'
down_revision: Union[str, None] = 'be60e42db4db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('alembic/versions/5ea413542a49_create_views.sql', 'r') as file:
        sql_commands = file.read()

    # Execute SQL from file
    op.execute(sql_commands)


def downgrade() -> None:
    drop_sql = ''
    with open('alembic/versions/5ea413542a49_create_views.sql', 'r') as file:
        for line in file:
            if 'drop' in line.lower():
                drop_sql += line
    print(f'The following sql code will be executed for downgrade:\n {drop_sql}')
    op.execute(drop_sql)    

