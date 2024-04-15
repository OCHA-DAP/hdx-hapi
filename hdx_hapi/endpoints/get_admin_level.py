from typing import List, Annotated
from fastapi import Depends, Query, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.admin_level import Admin1Response, Admin2Response, LocationResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.admin1_logic import get_admin1_srv
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Locations and Administrative Divisions'],
)


@router.get(
    '/api/location',
    response_model=List[LocationResponse],
    summary='Get the list of locations (typically countries) included in HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/location',
    response_model=List[LocationResponse],
    summary='Get the list of locations (typically countries) included in HAPI',
)
async def get_locations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE}')] = None,
    name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    result = await get_locations_srv(pagination_parameters=pagination_parameters, db=db, code=code, name=name)
    return transform_result_to_csv_stream_if_requested(result, output_format, LocationResponse)


get_locations.__doc__ = (
    'Not all data are available for all locations. Learn more about the scope of data coverage in HAPI in '
    f'the <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}">Overview and Getting Started</a> documentation.'
)


@router.get(
    '/api/admin1',
    response_model=List[Admin1Response],
    summary='Get the list of first-level subnational administrative divisions available in HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/admin1',
    response_model=List[Admin1Response],
    summary='Get the list of first-level subnational administrative divisions available in HAPI',
)
async def get_admin1(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE}')] = None,
    name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    result = await get_admin1_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin1Response)


get_admin1.__doc__ = (
    'Not all data are available for all locations. Learn more about the scope of data coverage in HAPI in '
    f'the <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}">Overview and Getting Started</a> documentation.'
)


@router.get(
    '/api/admin2',
    response_model=List[Admin2Response],
    summary='Get the list of second-level administrative divisions available in HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/admin2',
    response_model=List[Admin2Response],
    summary='Get the list of second-level administrative divisions available in HAPI',
)
async def get_admin2(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE}')] = None,
    name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    result = await get_admin2_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin2Response)


get_admin2.__doc__ = (
    'Not all data are available for all locations. Learn more about the scope of data coverage in HAPI in '
    f'the <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}">Overview and Getting Started</a> documentation.'
)
