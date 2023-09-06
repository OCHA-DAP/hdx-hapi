from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.location_view import LocationViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['location'],
)

@router.get('/api/location', response_model=List[LocationViewPydantic])
async def get_locations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10)] = None,
    name: Annotated[str, Query(max_length=10)] = None,
    reference_period_start: Annotated[str, Query()] = None,
    reference_period_end: Annotated[str, Query()] = None,
):
    result = await get_locations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result
