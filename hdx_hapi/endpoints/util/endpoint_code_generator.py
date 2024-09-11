#!/usr/bin/env python
# encoding: utf-8

"""
This is a prototype script for generating various code fragments for adding a new endpoint to hapi

Ian Hopkinson 2024-09-11
"""

endpoint_name = 'idps'

type_lookup = {
    'admin1_ref': 'int',
    'admin2_ref': 'int',
    'provider_admin1_name': 'str|512',
    'provider_admin2_name': 'str|512',
    'reference_period_start': '',
    'reference_period_end': '',
    'location_code': 'str|128',
    'location_name': 'str|512',
    'has_hrp': 'bool',
    'in_gho': 'bool',
    'admin1_code': 'str|128',
    'admin1_name': 'str|512',
    'admin2_code': 'str|128',
    'admin2_name': 'str|512',
}
doc_lookup = {
    'admin1_ref': 'DOC_ADMIN1_REF',
    'admin2_ref': 'DOC_ADMIN2_REF',
    'provider_admin1_name': 'DOC_PROVIDER_ADMIN1_NAME',
    'provider_admin2_name': 'DOC_PROVIDER_ADMIN2_NAME',
    'reference_period_start': '',
    'reference_period_end': '',
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
    print(f'from hdx_hapi.services.{endpoint_name}_logic import get_{endpoint_name.title()}_srv', flush=True)


def routes_in_main():
    print('These statements go in main.py, in the root of repo', flush=True)

    print(f'\nfrom hdx_hapi.endpoints.get_{endpoint_name} import router as {endpoint_name}_router  # noqa', flush=True)
    print(f'app.include_router({endpoint_name}_router)', flush=True)


if __name__ == '__main__':
    main()
