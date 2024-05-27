from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.currency_view_dao import currencies_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_currencies_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
):
    return await currencies_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
    )
