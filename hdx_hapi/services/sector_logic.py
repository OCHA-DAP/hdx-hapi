from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.sector_view_dao import sectors_view_list

from datetime import datetime


async def get_sectors_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):
    return await sectors_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end
    )
