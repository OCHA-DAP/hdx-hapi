from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.age_range_view_dao import age_ranges_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_age_ranges_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
):
    return await age_ranges_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
    )
