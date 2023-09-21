from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.age_range_view import AgeRangeViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.age_range_logic import get_age_ranges_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['demographics'],
)

@router.get('/api/age_range', response_model=List[AgeRangeViewPydantic])
async def get_age_ranges(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Age range code', example='20-24')] = None,
    age_min: Annotated[int, Query(ge=0, description='Minimum age', example=10)] = None,
    age_max: Annotated[int, Query(ge=0, description='Maximum age', example=50)] = None
):
    """Get the list of all active age ranges.
    """    
    result = await get_age_ranges_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        age_min=age_min,
        age_max=age_max
    )
    return result
