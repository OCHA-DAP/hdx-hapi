from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.sector_view_dao import sectors_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_sectors_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
):
    return await sectors_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
    )
