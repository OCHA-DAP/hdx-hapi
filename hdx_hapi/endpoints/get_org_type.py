from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.org_type_view import OrgTypeViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.org_type_logic import get_org_types_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['humanitarian_response'],
)

@router.get('/api/org_type', response_model=List[OrgTypeViewPydantic])
async def get_org_types(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Organization type code', example='123')] = None,
    description: Annotated[str, Query(max_length=50, description='Organization type description', example='Government')] = None
):
    """Get the list of all active organisation types.
    """    
    result = await get_org_types_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )
    return result
