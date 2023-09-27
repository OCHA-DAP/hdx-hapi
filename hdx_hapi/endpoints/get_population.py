from datetime import datetime, date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.population_view import PopulationViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['population'],
)


@router.get('/api/population', response_model=List[PopulationViewPydantic])
async def get_populations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    gender_code: Annotated[str, Query(max_length=1, description='Gender code')] = None,
    age_range_code: Annotated[str, Query(max_length=32, description='Ange range code')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    dataset_provider_code: Annotated[str, Query(max_length=128, description='Dataset ID given by provider')] = None,
    resource_update_date: Annotated[datetime | date, Query(description='Resource update date', example='2023-01-01T23:59:59')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    admin1_is_unspecified: Annotated[bool, Query(description='Is admin1 specified or not')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Admin2 code')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Admin2 name')] = None,
    admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,
):
    """
    Return the list of populations
    """
    result = await get_populations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        gender_code=gender_code,
        age_range_code=age_range_code,
        population=population,
        dataset_provider_code=dataset_provider_code,
        resource_update_date=resource_update_date,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
    )
    return result
