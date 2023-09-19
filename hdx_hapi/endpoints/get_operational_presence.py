from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.operational_presence_view import OperationalPresenceViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.operational_presence_logic import get_operational_presences_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['3W'],
)

@router.get('/api/themes/3W', response_model=List[OperationalPresenceViewPydantic])
async def get_operational_presences(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    org_ref: Annotated[int, Query(ge=1, description='Organization reference')] = None,
    location_name: Annotated[str, Query(max_length=10, description='Location name')] = None,
):
    """
    Get the list of operational presences.
    """
    result = await get_operational_presences_srv(pagination_parameters=pagination_parameters, db=db, org_ref=org_ref, location_name=location_name)
    return result
