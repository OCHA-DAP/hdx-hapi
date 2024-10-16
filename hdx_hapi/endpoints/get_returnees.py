from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from hapi_schema.utils.enums import Gender, PopulationGroup
from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_POPULATION_GROUP,
    DOC_GENDER,
    DOC_AGE_RANGE,
    DOC_LOCATION_CODE,
    DOC_SEE_LOC,
    DOC_LOCATION_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
)
from hdx_hapi.endpoints.models.returnees import ReturneesResponse
from hdx_hapi.services.returnees_logic import get_returnees_srv

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)


CONFIG = get_config()
router = APIRouter(
    tags=['Affected People'],
)


@router.get(
    '/api/affected-people/returnees',
    response_model=HapiGenericResponse[ReturneesResponse],
    summary='Get returnees data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/affected-people/returnees',
    response_model=HapiGenericResponse[ReturneesResponse],
    summary='Get returnees data',
)
async def get_returnees(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    population_group: Annotated[Optional[PopulationGroup], Query(description=f'{DOC_POPULATION_GROUP}')] = None,
    gender: Annotated[Optional[Gender], Query(description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    min_age: Annotated[
        Optional[int],
        Query(
            ge=0,
            description='The minimum age from `age_range`, set to `null` if `age_range` is "all" and '
            'there is no age disaggregation',
        ),
    ] = None,
    max_age: Annotated[
        Optional[int],
        Query(
            ge=0,
            description=(
                'The maximum age from `age_range`, set to `null` if `age_range` is "all" and '
                'there is no age disaggregation, or if there is no upper limit to the '
                'age range'
            ),
        ),
    ] = None,
    origin_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    origin_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    origin_has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    origin_in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    asylum_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    asylum_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    asylum_has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    asylum_in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_returnees_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        population_group=population_group,
        gender=gender,
        age_range=age_range,
        min_age=min_age,
        max_age=max_age,
        origin_location_code=origin_location_code,
        origin_location_name=origin_location_name,
        origin_has_hrp=origin_has_hrp,
        origin_in_gho=origin_in_gho,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
        asylum_has_hrp=asylum_has_hrp,
        asylum_in_gho=asylum_in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, ReturneesResponse)
