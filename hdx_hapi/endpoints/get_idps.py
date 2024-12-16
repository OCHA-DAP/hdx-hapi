from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
)
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    common_date_range_params,
    common_endpoint_parameters,
    common_location_parameters,
)


from hdx_hapi.endpoints.models.idps import IdpsResponse
from hdx_hapi.services.idps_logic import get_idps_srv

CONFIG = get_config()
router = APIRouter(
    tags=['Affected People'],
)


@router.get(
    '/api/affected-people/idps',
    response_model=HapiGenericResponse[IdpsResponse],
    summary='Get idps data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/affected-people/idps',
    response_model=HapiGenericResponse[IdpsResponse],
    responses=ERROR_RESPONSES,  # type: ignore
    summary='Get idps data',
)
async def get_idps(
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_idps_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, IdpsResponse)
