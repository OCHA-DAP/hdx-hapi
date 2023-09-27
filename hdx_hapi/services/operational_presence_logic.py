from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.operational_presence_view_dao import operational_presences_view_list


async def get_operational_presences_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    sector_code=None,
    dataset_provider_code=None,
    org_acronym=None,
    org_name=None,
    sector_name=None,
    location_code=None,
    location_name=None,
    admin1_code=None,
    admin1_is_unspecified=None,
    admin2_code=None,
    admin2_name=None,
    admin2_is_unspecified=None,
):
    return await operational_presences_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        sector_code=sector_code, 
        dataset_provider_code=dataset_provider_code,
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
    )
