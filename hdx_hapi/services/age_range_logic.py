from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.age_range_view_dao import age_ranges_view_list


async def get_age_ranges_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    age_min: int = None,
    age_max: int = None
):
    return await age_ranges_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        age_min=age_min,
        age_max=age_max
    )
