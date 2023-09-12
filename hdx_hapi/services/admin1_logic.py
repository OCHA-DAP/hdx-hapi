from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin1_view_dao import admin1_view_list

from datetime import datetime


async def get_admin1_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    is_unspecified: bool = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):
    return await admin1_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        is_unspecified=is_unspecified,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
    )
