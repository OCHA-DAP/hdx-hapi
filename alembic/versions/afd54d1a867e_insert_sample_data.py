"""insert sample data

Revision ID: afd54d1a867e
Revises: 5ea413542a49
Create Date: 2023-09-07 20:59:47.907634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afd54d1a867e'
down_revision: Union[str, None] = '5ea413542a49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('alembic/versions/afd54d1a867e_insert_sample_data.sql', 'r') as file:
        sql_commands = file.read()

    # Execute SQL from file
    op.execute(sql_commands)


def downgrade() -> None:
    truncate_sql = ''
    with open('alembic/versions/afd54d1a867e_insert_sample_data.sql', 'r') as file:
        for line in file:
            line = line.lower().strip()
            if line.startswith('insert into'):
                table_name = line.split(' ')[2]
                truncate_sql += f'TRUNCATE TABLE {table_name} CASCADE; \n'
            
    print(f'The following sql code will be executed for downgrade:\n {truncate_sql}')
    op.execute(truncate_sql)
