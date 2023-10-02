from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.location_view_dao import locations_view_list


async def get_locations_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
):
    return await locations_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
    )
