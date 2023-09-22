from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.operational_presence_view_dao import operational_presences_view_list


async def get_operational_presences_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    org_ref: int = None,
    dataset_hdx_id: str = None,
    dataset_hdx_stub: str = None,
    # dataset_title: str = None,
    dataset_provider_code: str = None,
    # dataset_provider_name: str = None,
    # resource_hdx_id: str = None,
    # resource_filename: str = None,
    org_acronym: str = None,
    org_name: str = None,
    # org_type_code: str = None,
    # org_type_description: str = None,
    sector_name: str = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    admin2_code: str = None,
    admin2_name: str = None,
):
    return await operational_presences_view_list(
        pagination_parameters=pagination_parameters, 
        db=db, 
        org_ref=org_ref, 
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub, 
        # dataset_title=dataset_title, 
        dataset_provider_code=dataset_provider_code,
        # dataset_provider_name=dataset_provider_name, 
        # resource_hdx_id=resource_hdx_id,
        # resource_filename=resource_filename, 
        org_acronym=org_acronym,
        org_name=org_name, 
        # org_type_code=org_type_code,
        # org_type_description=org_type_description, 
        sector_name=sector_name, 
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code, 
        admin1_name=admin1_name,
        admin2_code=admin2_code, 
        admin2_name=admin2_name,
    )
