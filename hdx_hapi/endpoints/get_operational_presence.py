from datetime import datetime, date
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
    sector_code: Annotated[str, Query(max_length=512, description='Sector Code')] = None,
    dataset_provider_code: Annotated[str, Query(max_length=128, description='Dataset Provider Name')] = None,
    resource_update_date_min: Annotated[datetime | date, Query(description='Min date of update date', example='2022-01-01T00:00:00')] = None,
    resource_update_date_max: Annotated[datetime | date, Query(description='Max date of update date', example='2022-01-01T23:59:59')] = None,
    org_acronym: Annotated[str, Query(max_length=32, description='Organization Acronym')] = None,
    org_name: Annotated[str, Query(max_length=512, description='Organization Name')] = None,
    sector_name: Annotated[str, Query(max_length=512, description='Sector Name')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location Code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location Name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Location Adm1 Code')] = None,
    admin1_is_unspecified: Annotated[bool, Query(description='Location Adm1 is not specified')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Location Adm2 Code')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Location Adm2 Name')] = None,
    admin2_is_unspecified: Annotated[bool, Query(description='Location Adm2 is not specified')] = None,
    # org_ref: Annotated[int, Query(ge=1, description='Organization reference')] = None,
    # dataset_hdx_id: Annotated[str, Query(max_length=36, description='HDX Dataset ID')] = None,
    # dataset_hdx_stub: Annotated[str, Query(max_length=128, description='HDX Dataset Name')] = None,
    # dataset_title: Annotated[str, Query(max_length=1024, description='Location name')] = None,
    # dataset_provider_name: Annotated[str, Query(max_length=512, description='Location name')] = None,
    # resource_hdx_id: Annotated[str, Query(max_length=36, description='Location name')] = None,
    # resource_filename: Annotated[str, Query(max_length=256, description='Location name')] = None,
    # org_type_code: Annotated[str, Query(max_length=32, description='Location name')] = None,
    # org_type_description: Annotated[str, Query(max_length=512, description='Location name')] = None,
    # admin1_name: Annotated[str, Query(max_length=512, description='Location Adm1 Name')] = None,


):
    """
    Get the list of operational presences.
    """
    result = await get_operational_presences_srv(
        pagination_parameters=pagination_parameters, 
        db=db, 
        sector_code=sector_code, 
        dataset_provider_code=dataset_provider_code,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name, 
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code, 
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code, 
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified 
        # dataset_hdx_id=dataset_hdx_id,
        # dataset_hdx_stub=dataset_hdx_stub, 
        # dataset_title=dataset_title, 
        # dataset_provider_name=dataset_provider_name, 
        # resource_hdx_id=resource_hdx_id,
        # resource_filename=resource_filename, 
        # org_type_code=org_type_code,
        # org_type_description=org_type_description, 

        )
    return result
