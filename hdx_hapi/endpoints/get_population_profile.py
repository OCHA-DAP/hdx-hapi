from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.population_profile import PopulationGroupResponse, PopulationStatusResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_group_logic import get_population_groups_srv
from hdx_hapi.services.population_status_logic import get_population_statuses_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Population Groups and Statuses'],
)


@router.get('/api/population_group', response_model=List[PopulationGroupResponse], summary='Get population groups data')
async def get_population_groups(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Population group code')] = None,
    description: Annotated[str, Query(max_length=512, description='Population group description')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of population groups
    """
    result = await get_population_groups_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationGroupResponse)


@router.get('/api/population_status', response_model=List[PopulationStatusResponse],
            summary='Get population statuses data')
async def get_population_statuses(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Population status code')] = None,
    description: Annotated[str, Query(max_length=512, description='Population status description')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of population statuses
    """
    result = await get_population_statuses_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationStatusResponse)
