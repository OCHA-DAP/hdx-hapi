from typing import Annotated
from fastapi import Depends, Query, APIRouter

from hdx_hapi.config.config import get_config
from sqlalchemy.ext.asyncio import AsyncSession
from hapi_schema.utils.enums import IPCPhase, IPCType
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.food_security import FoodSecurityResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
    AdminLevel,
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
    summary='Get food security data',
)
async def get_food_security(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    db: AsyncSession = Depends(get_db),
    ipc_phase: Annotated[IPCPhase, Query(description='IPC Phase')] = None,
    ipc_type: Annotated[IPCType, Query(description='IPC Type')] = None,
    location_ref: Annotated[int, Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_ref: Annotated[int, Query(description=f'{DOC_ADMIN1_REF}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Location Adm1 is not specified')] = None,
    admin2_ref: Annotated[int, Query(description=f'{DOC_ADMIN2_REF}')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level.')] = None,
    # admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_food_security_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        ipc_phase=ipc_phase,
        ipc_type=ipc_type,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        location_ref=location_ref,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, FoodSecurityResponse)


get_food_security.__doc__ = (
    'Integrated Food Security Phase Classification from the IPC. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'food_security_and_nutrition/#food-security">HDX HAPI documentation</a>, '
    'and the <a href="https://www.ipcinfo.org/ipcinfo-website/'
    'ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/">'
    'original IPC source</a> website.'
)
