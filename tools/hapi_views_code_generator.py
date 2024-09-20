#!/usr/bin/env python
# encoding: utf-8
"""
This script is designed to generate view tables, originally it lived in the hapi-sqlalchemy-schema repo.
It needs to be run inside the hapi Docker container so that it can access the hapi_test database.
The test database docker container needs to be started and initialised for this code to run.

The code is configured using the `view_as_table_definitions.toml` file and then with an invocation like:

`python hapi_views_code_generator.py wfp_commodity_view`

or

`./hapi_views_code_generator.py all`

The assumption is that the view_as_table_definitions.toml file will have been edited appropriately when generating the
"views as table". This script generates the imports, setups and classes for all views in a single run - they
can be piped to a file or a single view

Currently this script and the endpoint_code_generator.py script use separate toml files for configuration.

Ian Hopkinson 2024-09-20
"""

import os
import sys

sys.path.append('..')
from importlib import import_module

import psycopg
import sqlalchemy
import tomli
from hdx.database import Database


# Edit this to import the view parameters
from hapi_schema.utils.base import Base
from hapi_schema.views import prepare_hapi_views
from hdx_hapi.config.config import get_config


def parse_toml():
    # Setup the database:
    session = make_session()
    Base.metadata.create_all(session.get_bind())
    Base.metadata.reflect(bind=session.get_bind(), views=True)
    target_view = None
    if len(sys.argv) == 2:
        target_view = sys.argv[1]
    else:
        target_view = 'all'

    config_file_path = os.path.join(os.path.dirname(__file__), 'view_as_table_definitions.toml')
    with open(config_file_path, 'rb') as file_handle:
        config = tomli.load(file_handle)

    complete_code = []
    # Description
    complete_code.append('"""')
    complete_code.append(
        'This code was generated automatically using src/hapi_schema/utils/hapi_views_code_generator.py'
    )
    complete_code.append('"""')

    # Make imports
    complete_code.append('from decimal import Decimal')
    complete_code.append('from sqlalchemy import DateTime')
    complete_code.append('from sqlalchemy.orm import column_property, Mapped')

    complete_code.append('from hapi_schema.db_admin1 import view_params_admin1')

    complete_code.append('from hdx_hapi.db.models.views.util.util import view')
    complete_code.append('from hdx_hapi.db.models.base import Base')

    if target_view == 'all':
        for table in config['tables']:
            complete_code.append(f"from hapi_schema.{table['db_module']} import {table['view_params_name']}")

    complete_code.append('\n')
    # Make views
    if target_view == 'all':
        for table in config['tables']:
            complete_code.append(
                f"{table['target_view']} = view({table['view_params_name']}.name, "
                f"Base.metadata, {table['view_params_name']}.selectable)"
            )

    complete_code.append('\n')
    # Loop over tables
    for table in config['tables']:
        if target_view == 'all':
            table_code = create_table_code(table, target_view)
            complete_code.extend(table_code)
        elif table['target_view'] == target_view:
            complete_code = create_table_code(table, target_view)

    for line in complete_code:
        print(line, flush=True)


def create_table_code(
    parameters: dict,
    table_view: str = None,
) -> list[str]:
    # Change these the target_view, prepare_view, expected_primary_keys and expected_indexes
    target_view = parameters['target_view']
    expected_primary_keys = parameters['expected_primary_keys']
    expected_indexes = parameters['expected_indexes']
    expected_nullables = parameters['expected_nullables']

    view_params_dict = dynamically_load_view_params(parameters['db_module'], parameters['view_params_name'])
    _ = Database.prepare_view(view_params_dict)
    #

    columns = Base.metadata.tables[target_view].columns
    target_table = target_view.replace('view', 'vat')
    # Make Preamble
    table_code = []

    _, table_body_code = make_table_template_from_view(
        target_table,
        columns,
        expected_indexes=expected_indexes,
        expected_nullables=expected_nullables,
        expected_primary_keys=expected_primary_keys,
    )

    table_code.extend(table_body_code)

    return table_code


def make_table_template_from_view(
    target_table,
    columns,
    expected_indexes=None,
    expected_primary_keys=None,
    expected_nullables=None,
):
    if expected_primary_keys is None:
        expected_primary_keys = ['id']
    if expected_indexes is None:
        expected_indexes = []
    if expected_nullables is None:
        expected_nullables = []

    table_code = []
    # Make a CamelCase name from the supplied table name
    # admin1_vat-> Admin1View
    class_name = target_table.replace('_vat', '').replace('_', ' ').title().replace(' ', '') + 'View'

    source_view = target_table.replace('_vat', '_view')
    table_code.append(f'\nclass {class_name}(Base):')
    table_code.append(f'    __table__ = {source_view}')

    new_columns = []
    for column in columns:
        new_column = column._copy()
        column_type = str(column.type)
        mapped_type_1 = column_type
        if column_type == 'INTEGER':
            mapped_type_1 = 'int'
        elif column_type.startswith('VARCHAR'):
            mapped_type_1 = 'str'
        elif column_type == 'BOOLEAN':
            mapped_type_1 = 'bool'
        elif column_type in ['DATETIME', 'TIMESTAMP']:
            mapped_type_1 = 'DateTime'
        elif column_type in ['FLOAT', 'DOUBLE PRECISION']:
            mapped_type_1 = 'float'
        elif column_type == 'TEXT':
            mapped_type_1 = 'str'
        elif column_type == 'NUMERIC':
            mapped_type_1 = 'Decimal'
        table_code.append(
            f'    {column.name}: Mapped[{mapped_type_1}] = column_property({source_view}.c.{column.name})'
        )

        new_columns.append(new_column)
    return new_columns, table_code


def make_session():
    os.environ['HAPI_DB_NAME'] = 'hapi_test'
    db_uri = get_config().SQL_ALCHEMY_PSYCOPG2_DB_URI
    print(db_uri, flush=True)
    # db_uri = 'postgresql+psycopg://postgres:postgres@localhost:5432/hapi_test'
    session = None
    try:
        database = Database(db_uri=db_uri, recreate_schema=True, prepare_fn=prepare_hapi_views)
        session = database.get_session()
    except (psycopg.errors.DuplicateTable, sqlalchemy.exc.ProgrammingError):
        pass
    return session


def dynamically_load_view_params(db_module, view_name):
    module = import_module(f'hapi_schema.{db_module}')
    target_view_params = getattr(module, f'{view_name}')

    return target_view_params.__dict__


if __name__ == '__main__':
    parse_toml()
    # output_table_code_to_stdout()
