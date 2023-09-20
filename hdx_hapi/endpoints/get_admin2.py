from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.admin2_view import Admin2ViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['geodata'],
)

@router.get('/api/admin2', response_model=List[Admin2ViewPydantic])
async def get_admin2(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10, description='Code')] = None,
    name: Annotated[str, Query(max_length=10, description='Name')] = None,
    is_unspecified: Annotated[bool, Query(description='Is specified or not')] = None,
    reference_period_start: Annotated[datetime | date, Query(description='Start date of reference period', example='2022-01-01T00:00:00')] = None,
    reference_period_end: Annotated[datetime | date, Query(description='End date of reference period', example='2023-01-01T23:59:59')] = None,
):
    """Get the list of admin2 entries.
    """    
    result = await get_admin2_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        is_unspecified=is_unspecified,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result