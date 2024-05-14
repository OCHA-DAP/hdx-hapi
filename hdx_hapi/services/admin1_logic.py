from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin1_view_dao import admin1_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_admin1_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    location_code: str = None,
    location_name: str = None,
):
    return await admin1_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )
