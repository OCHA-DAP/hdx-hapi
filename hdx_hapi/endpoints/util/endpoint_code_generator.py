#!/usr/bin/env python
# encoding: utf-8

"""
This is a prototype script for generating various code fragments for adding a new endpoint to hapi

Ian Hopkinson 2024-09-11
"""

endpoint_name = 'idps'

type_lookup = {
    'resource_hdx_id': 'str|36',
    'reporting_round': 'int',
    'population': 'int',
    'assessment_type': 'DTMAssessmentType',
    'admin1_ref': 'int',
    'admin2_ref': 'int',
    'provider_admin1_name': 'str|512',
    'provider_admin2_name': 'str|512',
    'reference_period_start': 'datetime',
    'reference_period_end': 'Optional[datetime]',
    'location_code': 'str|128',
    'location_name': 'str|512',
    'has_hrp': 'bool',
    'in_gho': 'bool',
    'admin1_code': 'str|128',
    'admin1_name': 'str|512',
    'admin2_code': 'str|128',
    'admin2_name': 'str|512',
    'category': 'str|32',
    'subcategory': 'str|512',
}
doc_lookup = {
    'resource_hdx_id': 'DOC_HDX_RESOURCE_ID',
    'admin1_ref': 'DOC_ADMIN1_REF',
    'admin2_ref': 'DOC_ADMIN2_REF',
    'provider_admin1_name': 'DOC_PROVIDER_ADMIN1_NAME',
    'provider_admin2_name': 'DOC_PROVIDER_ADMIN2_NAME',
    'reference_period_start': 'DOC_REFERENCE_PERIOD_START',
    'reference_period_end': 'DOC_REFERENCE_PERIOD_END',
    'location_ref': 'LOCATION_REF',
    'location_code': 'DOC_LOCATION_CODE|DOC_SEE_LOC',
    'location_name': 'DOC_LOCATION_NAME|DOC_SEE_LOC',
    'has_hrp': 'DOC_LOCATION_HAS_HRP',
    'in_gho': 'DOC_LOCATION_IN_GHO',
    'admin1_code': 'DOC_ADMIN1_CODE|DOC_SEE_ADMIN1',
    'admin1_name': 'DOC_ADMIN1_NAME|DOC_SEE_ADMIN1',
    'admin2_code': 'DOC_ADMIN2_CODE|DOC_SEE_ADMIN2',
    'admin2_name': 'DOC_ADMIN2_NAME|DOC_SEE_ADMIN2',
}
# name, type, docstring
query_fields = [
    'admin2_ref',
    'provider_admin1_name',
    'provider_admin2_name',
    'reference_period_start',
    'reference_period_end',
    'location_code',
    'location_name',
    'has_hrp',
    'in_gho',
    'admin1_code',
    'admin1_name',
    'admin2_code',
    'admin2_name',
]

response_fields = [
    'resource_hdx_id',
    'admin2_ref',
    'provider_admin1_name',
    'provider_admin2_name',
    'reporting_round',
    'assessment_type',
    'population',
    'reference_period_start',
    'reference_period_end',
    'location_ref',
    'location_code',
    'location_name',
    'admin1_code',
    'admin1_name',
    'admin2_code',
    'admin2_name',
    'admin1_ref',
]


def main():
    # Generating the routes in main.py
    routes_in_main()

    # Generating the endpoint file
    print(f'\nNow create a file hdx_hapi/endpoints/get_{endpoint_name}.py', flush=True)

    # Generic imports
    imports_for_get_route()

    # Generate decorator call signature:
    get_route_decorate()

    # Generate call signature start:
    get_route_call_signature()

    # Generate body / return function
    get_route_body_and_return()

    # Now make the response class
    print(
        f'\nThe Response class goes in a file, hdx_hapi/endpoints/models/{endpoint_name}.py',
        flush=True,
    )
    add_response_class()

    # Now make the get_[endpoint]_srv
    print(f'\nThe service function goes in a file, hdx_hapi/services/{endpoint_name}_logic.py', flush=True)
    add_service()

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

    generate_query_function()

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


def generate_query_function():
    print('\nimport logging', flush=True)
    print('from typing import Optional, Sequence', flush=True)

    print('\nfrom sqlalchemy.ext.asyncio import AsyncSession', flush=True)
    print('from sqlalchemy import select', flush=True)

    print(f'\nfrom hdx_hapi.db.models.views.vat_or_view import {endpoint_name.title()}View', flush=True)
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
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        type_ = type_lookup.get(query_field, 'str|128').split('|')[0]
        print(f'\t{query_field}: Optional[{type_}] = None,', flush=True)

    print(f') -> Sequence[{endpoint_name.title()}View]:', flush=True)

    print(f'\n\tquery = select({endpoint_name.title()}View)', flush=True)

    print('\n\t#Query statements', flush=True)

    for query_field in query_fields:
        if query_field.startswith('reference_period'):
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

    print("\n\tlogger.debug(f'Executing SQL query: {query}')", flush=True)

    print('\n\tresult = await db.execute(query)', flush=True)
    print(f'\t{endpoint_name} = result.scalars().all()', flush=True)

    print(f"\n\tlogger.info(f'Retrieved {{len({endpoint_name})}} rows from the database')", flush=True)

    print(f'\n\treturn {endpoint_name}', flush=True)


def add_service():
    print('\nfrom typing import Optional, Sequence', flush=True)
    print('from sqlalchemy.ext.asyncio import AsyncSession', flush=True)

    print(f'from hdx_hapi.db.dao.{endpoint_name}_view_dao import {endpoint_name}_view_list', flush=True)
    print(f'from hdx_hapi.db.models.views.all_views import {endpoint_name.title()}View', flush=True)

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
    print(f'\treturn await {endpoint_name}_view_list(', flush=True)
    print('\t\tpagination_parameters=pagination_parameters,', flush=True)
    print('\t\tref_period_parameters=ref_period_parameters,', flush=True)
    print('\t\tdb=db,', flush=True)
    for query_field in query_fields:
        if query_field.startswith('reference_period'):
            continue
        print(f'\t\t{query_field}={query_field},', flush=True)
    print('\t)', flush=True)


def add_response_class():
    print(f'class {endpoint_name.title()}Response(HapiBaseModel):', flush=True)
    for response_field in response_fields:
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


def get_route_body_and_return():
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


def get_route_call_signature():
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
        doc_strings = doc_lookup.get(query_field, 'DOC__').split('|')

        doc_string = 'Placeholder Text'
        if len(doc_strings[0]) != 0:
            doc_string = ''
            for part in doc_strings:
                doc_string = doc_string + f'{{{part}}}'

        if type_ == 'str':
            print(
                f'\t{query_field}: Annotated['
                f"Optional[{type_}], Query(max_length={max_length}, description=f'{doc_string}')"
                '] = None,',
                flush=True,
            )
        elif type_ == 'int':
            print(
                f'\t{query_field}: Annotated[' f"Optional[{type_}], Query(description=f'{doc_string}')" '] = None,',
                flush=True,
            )
        elif type_ == 'bool':
            print(
                f'\t{query_field}: Annotated[' f"Optional[{type_}], Query(description=f'{doc_string}')" '] = None,',
                flush=True,
            )
        else:
            print(f'No query annotation for {type_}', flush=True)
            sys.exit()

    # Add the end part
    print('\toutput_format: OutputFormat = OutputFormat.JSON', flush=True)
    print('):', flush=True)


def get_route_decorate():
    print('\n', flush=True)
    for version in ['', '/v1']:
        print('@router.get(', flush=True)
        print(f"'/api{version}/affected-people/{endpoint_name}',", flush=True)
        print(f'response_model=HapiGenericResponse[{endpoint_name.title()}Response],', flush=True)
        print(f"summary='Get {endpoint_name} data',", flush=True)
        if version == '':
            print('include_in_schema=False,', flush=True)
        print(')', flush=True)


def imports_for_get_route():
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
    DOC_ADMIN2_REF,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_PROVIDER_ADMIN2_NAME,
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
CONFIG = get_config()
router = APIRouter(
    tags=['Affected people'],
)
""",
        flush=True,
    )

    # These imports are per endpoint
    print(f'\nfrom hdx_hapi.endpoints.models.{endpoint_name} import {endpoint_name.title()}Response', flush=True)
    print(f'from hdx_hapi.services.{endpoint_name}_logic import get_{endpoint_name}_srv', flush=True)


def routes_in_main():
    print('These statements go in main.py, in the root of repo', flush=True)

    print(f'\nfrom hdx_hapi.endpoints.get_{endpoint_name} import router as {endpoint_name}_router  # noqa', flush=True)
    print(f'app.include_router({endpoint_name}_router)', flush=True)


if __name__ == '__main__':
    main()
