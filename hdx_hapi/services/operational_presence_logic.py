from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.operational_presence_view_dao import operational_presences_view_list


async def get_operational_presences_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    org_ref: int = None,
    location_name: str = None,
):
    return await operational_presences_view_list(
        pagination_parameters=pagination_parameters, db=db, org_ref=org_ref, location_name=location_name
    )
