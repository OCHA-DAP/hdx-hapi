from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.operationalpresenceview import OperationalPresenceViewPydantic
from hdx_hapi.services.operational_presence_logic import get_operational_presences_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['3W'],
)

@router.get('/api/themes/3W', response_model=List[OperationalPresenceViewPydantic])
async def get_operational_presences(
    db: AsyncSession = Depends(get_db),
    org_ref: Annotated[int, Query(gt=0)] = None,
    location_name: Annotated[str, Query(max_length=10)] = None,
):
    """
    This is the most important endpoint
    """
    result = await get_operational_presences_srv(db=db, org_ref=org_ref, location_name=location_name)
    return result
