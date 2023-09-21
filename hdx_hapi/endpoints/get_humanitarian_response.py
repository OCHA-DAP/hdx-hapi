from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.org_view import OrgViewPydantic
from hdx_hapi.endpoints.models.org_type_view import OrgTypeViewPydantic
from hdx_hapi.endpoints.models.sector_view import SectorViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.org_logic import get_orgs_srv
from hdx_hapi.services.org_type_logic import get_org_types_srv
from hdx_hapi.services.sector_logic import get_sectors_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['humanitarian-response'],
)

@router.get('/api/org', response_model=List[OrgViewPydantic])
async def get_orgs(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    acronym: Annotated[str, Query(max_length=10, description='Organization acronym', example='HDX')] = None,
    name: Annotated[str, Query(max_length=10, description='Organization name', example='Humanitarian Data Exchange')] = None,
    reference_period_start: Annotated[datetime | date, Query(description='Start date of reference period', example='2022-01-01T00:00:00')] = None,
    reference_period_end: Annotated[datetime | date, Query(description='End date of reference period', example='2023-01-01T23:59:59')] = None,
):
    """Get the list of all active organisations.
    """    
    result = await get_orgs_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        acronym=acronym,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result

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

@router.get('/api/sector', response_model=List[SectorViewPydantic])
async def get_sectors(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Sector code', example='HEA')] = None,
    name: Annotated[str, Query(max_length=50, description='Sector name', example='Health')] = None,
    reference_period_start: Annotated[datetime | date, Query(description='Start date of reference period', example='2022-01-01T00:00:00')] = None,
    reference_period_end: Annotated[datetime | date, Query(description='End date of reference period', example='2023-01-01T23:59:59')] = None,
):
    """Get the list of all active sectors.
    """    
    result = await get_sectors_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
    return result
