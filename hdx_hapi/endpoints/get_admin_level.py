from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_SCOPE_DISCLAIMER,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_LOCATION_CODE,
    DOC_LOCATION_ID,
    DOC_LOCATION_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
    DOC_LOCATION_REF,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.admin_level import Admin1Response, Admin2Response, LocationResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
)
from hdx_hapi.services.admin1_logic import get_admin1_srv
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Metadata'],
)


@router.get(
    '/api/metadata/location',
    response_model=HapiGenericResponse[LocationResponse],
    summary='Get the list of locations (typically countries) included in HDX HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/location',
    response_model=HapiGenericResponse[LocationResponse],
    summary='Get the list of locations (typically countries) included in HDX HAPI',
)
async def get_location(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    id: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    code: Annotated[Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE}')] = None,
    name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME}')] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_locations_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        code=code,
        name=name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, LocationResponse)


get_location.__doc__ = DOC_SCOPE_DISCLAIMER


@router.get(
    '/api/metadata/admin1',
    response_model=HapiGenericResponse[Admin1Response],
    summary='Get the list of first-level subnational administrative divisions available in HDX HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/admin1',
    response_model=HapiGenericResponse[Admin1Response],
    summary='Get the list of first-level subnational administrative divisions available in HDX HAPI',
)
async def get_admin1(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    id: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_ID}')] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    code: Annotated[Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE}')] = None,
    name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME}')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_admin1_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        location_ref=location_ref,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin1Response)


get_admin1.__doc__ = DOC_SCOPE_DISCLAIMER


@router.get(
    '/api/metadata/admin2',
    response_model=HapiGenericResponse[Admin2Response],
    summary='Get the list of second-level administrative divisions available in HDX HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/admin2',
    response_model=HapiGenericResponse[Admin2Response],
    summary='Get the list of second-level administrative divisions available in HDX HAPI',
)
async def get_admin2(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    id: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_ID}')] = None,
    admin1_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    code: Annotated[Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE}')] = None,
    name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME}')] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_admin2_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin2Response)


get_admin2.__doc__ = DOC_SCOPE_DISCLAIMER
