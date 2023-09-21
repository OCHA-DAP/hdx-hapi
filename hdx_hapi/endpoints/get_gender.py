from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.gender_view import GenderViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.gender_logic import get_genders_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['demographics'],
)

@router.get('/api/gender', response_model=List[GenderViewPydantic])
async def get_genders(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=1, description='Gender code', example='m')] = None,
    description: Annotated[str, Query(max_length=50, description='Gender description', example='female')] = None
):
    """Get the list of all genders.
    """    
    result = await get_genders_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )
    return result
