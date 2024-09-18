#!/usr/bin/env python
# encoding: utf-8

"""
This is a prototype script for generating various code fragments for adding a new endpoint to hapi

Ian Hopkinson 2024-09-11
"""

from typing import Optional
import os
import tomllib
import sys

type_lookup = {
    'resource_hdx_id': 'str|36',
    'reporting_round': 'int',
    'population': 'int',
    'assessment_type': 'DTMAssessmentType',
    'admin1_ref': 'int',
    'admin2_ref': 'int',
    'provider_admin1_name': 'str|512',
    'provider_admin2_name': 'str|512',
    'reference_period_start': 'datetime.datetime',
    'reference_period_end': 'Optional[datetime.datetime]',
    'location_ref': 'int',
    'location_code': 'str|128',
    'location_name': 'str|512',
    'has_hrp': 'bool',
    'in_gho': 'bool',
    'admin1_code': 'str|128',
    'admin1_name': 'str|512',
    'admin2_code': 'str|128',
    'admin2_name': 'str|512',
    'admin_level': 'AdminLevel',
    'category': 'str|32',
    'subcategory': 'str|512',
    # Returnees entries
    'origin_location_ref': 'int',
    'asylum_location_ref': 'int',
    'population_group': 'PopulationGroup',
    'gender': 'Gender',
    'age_range': 'str|32',
    'min_age': 'int',
    'max_age': 'int',
    'origin_location_code': 'str|128',
    'origin_location_name': 'str|512',
    'origin_has_hrp': 'bool',
    'origin_in_gho': 'bool',
    'asylum_location_code': 'str|128',
    'asylum_location_name': 'str|512',
    'asylum_has_hrp': 'bool',
    'asylum_in_gho': 'bool',
}

HapiModelWithAdmins_fields = [
    'location_ref',
    'location_code',
    'location_name',
    'admin1_ref',
    'admin1_code',
    'admin1_name',
    'admin2_ref',
    'admin2_code',
    'admin2_name',
    'admin1_is_unspecified',
    'admin2_is_unspecified',
]

doc_lookup = {
    'resource_hdx_id': 'DOC_HDX_RESOURCE_ID',
    'admin1_ref': 'DOC_ADMIN1_REF',
    'admin2_ref': 'DOC_ADMIN2_REF',
    'provider_admin1_name': 'DOC_PROVIDER_ADMIN1_NAME',
    'provider_admin2_name': 'DOC_PROVIDER_ADMIN2_NAME',
    'reference_period_start': 'DOC_REFERENCE_PERIOD_START',
    'reference_period_end': 'DOC_REFERENCE_PERIOD_END',
    'location_ref': 'DOC_LOCATION_REF',
    'location_code': 'DOC_LOCATION_CODE|DOC_SEE_LOC',
    'location_name': 'DOC_LOCATION_NAME|DOC_SEE_LOC',
    'has_hrp': 'DOC_LOCATION_HAS_HRP',
    'in_gho': 'DOC_LOCATION_IN_GHO',
    'admin1_code': 'DOC_ADMIN1_CODE|DOC_SEE_ADMIN1',
    'admin1_name': 'DOC_ADMIN1_NAME|DOC_SEE_ADMIN1',
    'admin2_code': 'DOC_ADMIN2_CODE|DOC_SEE_ADMIN2',
    'admin2_name': 'DOC_ADMIN2_NAME|DOC_SEE_ADMIN2',
    'admin_level': 'DOC_ADMIN_LEVEL_FILTER',
    'gender': 'DOC_GENDER',
    'population_group': 'DOC_POPULATION_GROUP',
}
# name, type, docstring


def main():
    #
    config = parse_toml(endpoint_name='idps')
    # Generating the routes in main.py
    endpoint_name = config['endpoint_name']
    query_fields = config['query_fields']
    response_fields = config['response_fields']
    has_HapiModelWithAdmins = config['has_HapiModelWithAdmins']

    routes_in_main(endpoint_name)

    # Generating the endpoint file
    print(f'\nNow create a file hdx_hapi/endpoints/get_{endpoint_name}.py', flush=True)
    print("It may be necessary to add enums  'from hapi_schema.utils.enums import '", flush=True)

    # Generic imports
    imports_for_get_route(endpoint_name)

    # Generate decorator call signature:
    get_route_decorate(endpoint_name)

    # Generate call signature start:
    get_route_call_signature(endpoint_name, query_fields)

    # Generate body / return function
    get_route_body_and_return(endpoint_name, query_fields)

    # Now make the response class
    print(
        f'\nThe Response class goes in a file, hdx_hapi/endpoints/models/{endpoint_name}.py',
        flush=True,
    )
    add_response_class(endpoint_name, response_fields, has_HapiModelWithAdmins)

    # Now make the get_[endpoint]_srv
    print(f'\nThe service function goes in a file, hdx_hapi/services/{endpoint_name}_logic.py', flush=True)
    add_service(endpoint_name, query_fields, has_HapiModelWithAdmins)

    # Generate the [Endpoint]View - this is done with code in the hapi-sqlalchemy-schema repo.
    print(f'\nThe {endpoint_name.title()}View goes in the file hdx_hapi/db/models/views/all_views.py file', flush=True)
    print('\nThis is generated using the hapi_schema/utils/hapi_views_code_generator.py code', flush=True)
    print('The following need to be added at the top of the all_views.py file', flush=True)
    print(
        f'from hapi_schema.db_{endpoint_name} import view_params_{endpoint_name}, availability_stmt_endpoint_name',
        flush=True,
    )
    print(
        f'{endpoint_name}_view = view(view_params_{endpoint_name}.name, Base.metadata, '
        f'view_params_{endpoint_name}.selectable)',
        flush=True,
    )

    print('The following need to be added to hdx_hapi/db/models/views/vat_or_view.py:', flush=True)
    print(f'{endpoint_name.title()}View', flush=True)
    print(f'DB{endpoint_name.title()}VAT as {endpoint_name.title()}View', flush=True)

    # Generate the query function
    print(
        f'\nThe query function is named {endpoint_name}_view_list and goes in the file '
        f'hdx_hapi/db/dao/{endpoint_name}_view_dao.py',
        flush=True,
    )

    generate_query_function(endpoint_name, query_fields, has_HapiModelWithAdmins)

    # Generate tests

    print(
        f'Next generate tests which need to go in a file tests/test_endpoints/tests_{endpoint_name}_endpoint.py.'
        'The easiest thing to do here is copy one of the existing files and do a search and replace on the endpoint '
        ' name',
        flush=True,
    )

    print(
        'Also required are a couple of test fixtures/additions. tests/test_endpoints/endpoint_data.py needs an '
        f'entry under the key /api/v1/affected-people/{endpoint_name} and a SQL file is also required with the name '
        f'tests/sample_data/{endpoint_name}.sql which needs adding to /srv/hapi/tests/conftest.py too',
        flush=True,
    )


def parse_toml(endpoint_name: Optional[str] = 'idps') -> dict:
    # Setup the database:
    if len(sys.argv) == 2:
        endpoint_name = sys.argv[1]

    config_file_path = os.path.join(os.path.dirname(__file__), 'endpoint_definitions.toml')
    with open(config_file_path, 'rb') as file_handle:
        all_config = tomllib.load(file_handle)

    requested_config = None
    for config in all_config['tables']:
        if config['endpoint_name'] == endpoint_name:
            requested_config = config
            break
    return requested_config


def generate_query_function(endpoint_name, query_fields, has_HapiModelWithAdmins):
    print('\nimport logging', flush=True)
    print('from typing import Optional, Sequence', flush=True)

    print('\nfrom sqlalchemy.ext.asyncio import AsyncSession', flush=True)
    print('from sqlalchemy import select', flush=True)

    print(f'\nfrom hdx_hapi.db.models.views.vat_or_view import {endpoint_name.title()}View', flush=True)

    if has_HapiModelWithAdmins:
        print(
            'from hdx_hapi.db.dao.util.util import apply_pagination, '
            'apply_reference_period_filter, case_insensitive_filter, apply_location_admin_filter',
            flush=True,
        )
    else:
        print(
            'from hdx_hapi.db.dao.util.util import apply_pagination, '
            'apply_reference_period_filter, case_insensitive_filter',
            flush=True,
        )
    print('from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters', flush=True)

    print('\nlogger = logging.getLogger(__name__)', flush=True)

    print(f'\nasync def {endpoint_name}_view_list(', flush=True)
    print('\tpagination_parameters: PaginationParams,', flush=True)
    print('\tref_period_parameters: ReferencePeriodParameters,', flush=True)
    print('\tdb: AsyncSession,', flush=True)
    if has_HapiModelWithAdmins:
        print('\tadmin1_is_unspecified: Optional[bool] = None,')
        print('\tadmin2_is_unspecified: Optional[bool] = None,')
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        if query_field == 'admin_level':
            continue
        type_ = type_lookup.get(query_field, 'str|128').split('|')[0]
        print(f'\t{query_field}: Optional[{type_}] = None,', flush=True)

    print(f') -> Sequence[{endpoint_name.title()}View]:', flush=True)

    print(f'\n\tquery = select({endpoint_name.title()}View)', flush=True)

    print('\n\t#Query statements', flush=True)

    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        if has_HapiModelWithAdmins and query_field in HapiModelWithAdmins_fields:
            continue
        if query_field == 'admin_level':
            continue
        type_ = type_lookup.get(query_field, 'str|128').split('|')[0]
        if query_field in ['has_hrp', 'in_gho']:
            print(f'\tif {query_field} is not None:', flush=True)
        else:
            print(f'\tif {query_field}:', flush=True)

        if type_ in ['int', 'bool']:
            print(f'\t\tquery = query.where({endpoint_name.title()}View.{query_field} == {query_field})', flush=True)
        elif type_ == 'str' and '_name' not in query_field:
            print(
                f'\t\tquery = case_insensitive_filter(query, {endpoint_name.title()}View.{query_field}, {query_field})',
                flush=True,
            )
        elif type_ == 'str' and '_name' in query_field:
            print(
                f'\t\tquery = query.where({endpoint_name.title()}View.{query_field}.icontains({query_field}))',
                flush=True,
            )
        else:
            print(f'\t\tquery = query.where({endpoint_name.title()}View.{query_field} == {query_field})', flush=True)

    print(
        f'\n\tquery = apply_reference_period_filter(query, ref_period_parameters, {endpoint_name.title()}View)',
        flush=True,
    )

    print('\tquery = apply_pagination(query, pagination_parameters)', flush=True)
    if has_HapiModelWithAdmins:
        print(
            '\tquery = apply_location_admin_filter('
            '\n\t\tquery,'
            f'\n\t\t{endpoint_name.title()}View,'
            '\n\t\tlocation_ref,'
            '\n\t\tlocation_code,'
            '\n\t\tlocation_name,'
            '\n\t\thas_hrp,'
            '\n\t\tin_gho,'
            '\n\t\tadmin1_ref,'
            '\n\t\tadmin1_code,'
            '\n\t\tadmin1_name,'
            '\n\t\tadmin1_is_unspecified,'
            '\n\t\tadmin2_ref,'
            '\n\t\tadmin2_code,'
            '\n\t\tadmin2_name,'
            '\n\t\tadmin2_is_unspecified,'
            '\n\t\t)',
            flush=True,
        )

    print("\n\tlogger.debug(f'Executing SQL query: {query}')", flush=True)

    print('\n\tresult = await db.execute(query)', flush=True)
    print(f'\t{endpoint_name} = result.scalars().all()', flush=True)

    print(f"\n\tlogger.info(f'Retrieved {{len({endpoint_name})}} rows from the database')", flush=True)

    print(f'\n\treturn {endpoint_name}', flush=True)


def add_service(endpoint_name, query_fields, has_HapiModelWithAdmins):
    print('\nfrom typing import Optional, Sequence', flush=True)
    print('from sqlalchemy.ext.asyncio import AsyncSession', flush=True)

    print(f'from hdx_hapi.db.dao.{endpoint_name}_view_dao import {endpoint_name}_view_list', flush=True)
    print(f'from hdx_hapi.db.models.views.all_views import {endpoint_name.title()}View', flush=True)

    if has_HapiModelWithAdmins:
        print(
            'from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams, ReferencePeriodParameters',
            flush=True,
        )
        print('from hdx_hapi.services.admin_level_logic import compute_unspecified_values', flush=True)
    else:
        print('from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters', flush=True)

    print(f'async def get_{endpoint_name}_srv(', flush=True)
    print('\tpagination_parameters: PaginationParams,', flush=True)
    print('\tref_period_parameters: ReferencePeriodParameters,', flush=True)
    print('\tdb: AsyncSession,', flush=True)
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        type_ = type_lookup.get(query_field, 'str|128').split('|')[0]
        print(f'\t{query_field}: Optional[{type_}] = None,', flush=True)
    print(f'\t) -> Sequence[{endpoint_name.title()}View]:', flush=True)
    if has_HapiModelWithAdmins:
        print('\tadmin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)')
    print(f'\treturn await {endpoint_name}_view_list(', flush=True)
    print('\t\tpagination_parameters=pagination_parameters,', flush=True)
    print('\t\tref_period_parameters=ref_period_parameters,', flush=True)
    if has_HapiModelWithAdmins:
        print('\t\tadmin1_is_unspecified=admin1_is_unspecified,', flush=True)
        print('\t\tadmin2_is_unspecified=admin2_is_unspecified,', flush=True)
    print('\t\tdb=db,', flush=True)
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        if query_field == 'admin_level':
            continue
        print(f'\t\t{query_field}={query_field},', flush=True)

    print('\t)', flush=True)


def add_response_class(endpoint_name, response_fields, has_HapiModelWithAdmins):
    if has_HapiModelWithAdmins:
        print(f'class {endpoint_name.title()}Response(HapiBaseModel, HapiModelWithAdmins):', flush=True)
    else:
        print(f'class {endpoint_name.title()}Response(HapiBaseModel):', flush=True)
    for response_field in response_fields:
        if has_HapiModelWithAdmins and response_field in HapiModelWithAdmins_fields:
            continue
        type_ = type_lookup.get(response_field, 'str|128').split('|')[0]
        try:
            max_length = type_lookup.get(response_field, 'str|128').split('|')[1]
        except IndexError:
            max_length = 1
        doc_string = doc_lookup.get(response_field, '"Placeholder text"').split('|')[0]

        if doc_string != '"Placeholder text"':
            doc_string = f'truncate_query_description({doc_string})'

        if type_ == 'str':
            print(f'\t{response_field}: {type_} = Field(max_length={max_length}, description={doc_string})', flush=True)
        elif 'datetime' in type_:
            print(f'\t{response_field}: {type_} = Field(description={doc_string})', flush=True)
        else:
            print(f'\t{response_field}: {type_} = Field(description={doc_string})', flush=True)

    print('\n\tmodel_config = ConfigDict(from_attributes=True)', flush=True)


def get_route_body_and_return(endpoint_name, query_fields):
    print('\tref_period_parameters = None', flush=True)
    print(
        f'\tresult = await get_{endpoint_name}_srv('
        '\n\t\tpagination_parameters=common_parameters,'
        '\n\t\tref_period_parameters=ref_period_parameters,'
        '\n\t\tdb=db,',
        flush=True,
    )
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        print(f'\t\t{query_field}={query_field},', flush=True)

    print(
        f'\t)\n\treturn transform_result_to_csv_stream_if_requested(result, output_format, '
        f'{endpoint_name.title()}Response)',
        flush=True,
    )


def get_route_call_signature(endpoint_name, query_fields):
    print(f'async def get_{endpoint_name}(', flush=True)
    print('\tcommon_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],', flush=True)

    print('\tdb: AsyncSession = Depends(get_db),', flush=True)
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        type_ = type_lookup.get(query_field, 'str|128').split('|')[0]
        try:
            max_length = type_lookup.get(query_field, 'str|128').split('|')[1]
        except IndexError:
            max_length = 1
        doc_strings = doc_lookup.get(query_field, "'Placeholder Text'").split('|')

        doc_string = "'Placeholder Text'"
        if 'placeholder' not in doc_strings[0].lower():
            doc_string = ''
            for part in doc_strings:
                doc_string = doc_string + f"f'{{{part}}}'"

        if type_ == 'str':
            print(
                f'\t{query_field}: Annotated['
                f'Optional[{type_}], Query(max_length={max_length}, description={doc_string})'
                '] = None,',
                flush=True,
            )
        else:
            print(
                f'\t{query_field}: Annotated[' f'Optional[{type_}], Query(description={doc_string})' '] = None,',
                flush=True,
            )

    # Add the end part
    print('\toutput_format: OutputFormat = OutputFormat.JSON', flush=True)
    print('):', flush=True)


def get_route_decorate(endpoint_name):
    print('\n', flush=True)
    for version in ['', '/v1']:
        print('@router.get(', flush=True)
        print(f"'/api{version}/affected-people/{endpoint_name}',", flush=True)
        print(f'response_model=HapiGenericResponse[{endpoint_name.title()}Response],', flush=True)
        print(f"summary='Get {endpoint_name} data',", flush=True)
        if version == '':
            print('include_in_schema=False,', flush=True)
        print(')', flush=True)


def imports_for_get_route(endpoint_name):
    print(
        """from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN_LEVEL_FILTER,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_NAME,
    DOC_ADMIN1_CODE,
    DOC_PROVIDER_ADMIN1_NAME,
    DOC_PROVIDER_ADMIN2_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
    DOC_SEE_ADMIN2,
)
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
    AdminLevel,
)
""",  # noqa
        flush=True,
    )
    # These imports are per endpoint
    print(f'\nfrom hdx_hapi.endpoints.models.{endpoint_name} import {endpoint_name.title()}Response', flush=True)
    print(f'from hdx_hapi.services.{endpoint_name}_logic import get_{endpoint_name}_srv', flush=True)

    print("CONFIG = get_config()\nrouter = APIRouter(\n\ttags=['Affected people'],)", flush=True)


def routes_in_main(endpoint_name):
    print('These statements go in main.py, in the root of repo', flush=True)

    print(f'\nfrom hdx_hapi.endpoints.get_{endpoint_name} import router as {endpoint_name}_router  # noqa', flush=True)
    print(f'app.include_router({endpoint_name}_router)', flush=True)


if __name__ == '__main__':
    main()
