from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.admin1_view import Admin1ViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.admin1_logic import get_admin1_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['location'],
)

@router.get('/api/admin1', response_model=List[Admin1ViewPydantic])
async def get_admin1(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10)] = None,
    name: Annotated[str, Query(max_length=10)] = None,
    is_unspecified: Annotated[bool, Query()] = None,
    reference_period_start: Annotated[datetime | date, Query()] = None,
    reference_period_end: Annotated[datetime | date, Query()] = None,
):
    result = await get_admin1_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        is_unspecified=is_unspecified,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result