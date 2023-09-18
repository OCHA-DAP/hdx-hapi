from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.admin2_view import Admin2ViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['location'],
)

@router.get('/api/admin2', response_model=List[Admin2ViewPydantic])
async def get_admin2(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10)] = None,
    name: Annotated[str, Query(max_length=10)] = None,
    is_unspecified: Annotated[bool, Query()] = None,
    reference_period_start: Annotated[datetime | date, Query()] = None,
    reference_period_end: Annotated[datetime | date, Query()] = None,
):
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