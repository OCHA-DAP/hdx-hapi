from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.admin1_view import Admin1ViewPydantic
from hdx_hapi.endpoints.models.admin2_view import Admin2ViewPydantic
from hdx_hapi.endpoints.models.location_view import LocationViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.admin1_logic import get_admin1_srv
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['admin-level'],
)

@router.get('/api/location', response_model=List[LocationViewPydantic])
async def get_locations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    name: Annotated[str, Query(max_length=512, description='Location name')] = None,
):
    """Get the list of locations.
    """    
    result = await get_locations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name
    )
    return result


@router.get('/api/admin1', response_model=List[Admin1ViewPydantic])
async def get_admin1(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description='Code')] = None,
    name: Annotated[str, Query(max_length=512, description='Name')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location name')] = None,
):
    """Get the list of admin1 entries.
    """    
    result = await get_admin1_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )
    return result


@router.get('/api/admin2', response_model=List[Admin2ViewPydantic])
async def get_admin2(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description='Code')] = None,
    name: Annotated[str, Query(max_length=512, description='Name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location name')] = None,
):
    """Get the list of admin2 entries.
    """    
    result = await get_admin2_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )
    return result
