from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from hdx_hapi.config.config import get_config
from sqlalchemy.ext.asyncio import AsyncSession
from hapi_schema.utils.enums import IPCPhase, IPCType
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_IPC_PHASE,
    DOC_IPC_TYPE,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.food_security import FoodSecurityResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    CommonLocationParameters,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
    common_location_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.food_security_logic import get_food_security_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()
router = APIRouter(
    tags=['Food Security & Nutrition'],
)


@router.get(
    '/api/food/food-security',
    response_model=HapiGenericResponse[FoodSecurityResponse],
    summary='Get food security data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/food/food-security',
    response_model=HapiGenericResponse[FoodSecurityResponse],
    responses=ERROR_RESPONSES, # type: ignore
    summary='Get food security data',
)
async def get_food_security(
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    db: AsyncSession = Depends(get_db),
    ipc_phase: Annotated[Optional[IPCPhase], Query(description=f'{DOC_IPC_PHASE}')] = None,
    ipc_type: Annotated[Optional[IPCType], Query(description=f'{DOC_IPC_TYPE}')] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_food_security_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        ipc_phase=ipc_phase,
        ipc_type=ipc_type,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, FoodSecurityResponse)


get_food_security.__doc__ = (
    'Integrated Food Security Phase Classification from the IPC. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'food_security_and_nutrition/#food-security">HDX HAPI documentation</a>, '
    'and the <a href="https://www.ipcinfo.org/ipcinfo-website/'
    'ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/">'
    'original IPC source</a> website.'
)
