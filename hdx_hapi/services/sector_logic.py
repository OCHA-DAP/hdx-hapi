from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.sector_view_dao import sectors_view_list


async def get_sectors_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
):
    return await sectors_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
    )
