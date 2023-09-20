from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.location_view import LocationViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['geodata'],
)

@router.get('/api/location', response_model=List[LocationViewPydantic])
async def get_locations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10, description='Location code')] = None,
    name: Annotated[str, Query(max_length=10, description='Location name')] = None,
    reference_period_start: Annotated[datetime | date, Query(description='Start date of reference period', example='2022-01-01T00:00:00')] = None,
    reference_period_end: Annotated[datetime | date, Query(description='End date of reference period', example='2023-01-01T23:59:59')] = None,
):
    """Get the list of locations.
    """    
    result = await get_locations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result
