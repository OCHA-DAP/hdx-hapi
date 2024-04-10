from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_UPDATE_DATE_MAX,
    DOC_UPDATE_DATE_MIN,
)

from hdx_hapi.endpoints.models.food_security import FoodSecurityResponse
from hdx_hapi.endpoints.util.util import AdminLevel, OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.food_security_logic import get_food_security_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Food Security'],
)


@router.get('/api/themes/food_security', response_model=List[FoodSecurityResponse], summary='Get food security data')
@router.get('/api/v1/themes/food_security', response_model=List[FoodSecurityResponse], summary='Get food security data')
async def get_food_security(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    ipc_phase_code: Annotated[str, Query(max_length=32, description='IPC phase code')] = None,
    ipc_type_code: Annotated[str, Query(max_length=32, description='IPC type code')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description='Organization(provider) code')] = None,
    resource_update_date_min: Annotated[
        NaiveDatetime | date, Query(description=f'{DOC_UPDATE_DATE_MIN}', example='2020-01-01')
    ] = None,
    resource_update_date_max: Annotated[
        NaiveDatetime | date, Query(description=f'{DOC_UPDATE_DATE_MAX}', example='2024-12-31')
    ] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Admin2 name')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Admin2 code')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of food security data
    """
    result = await get_food_security_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        ipc_phase_code=ipc_phase_code,
        ipc_type_code=ipc_type_code,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, FoodSecurityResponse)
