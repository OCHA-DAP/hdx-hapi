from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.org_view_dao import orgs_view_list

from datetime import datetime


async def get_orgs_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    acronym: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):
    return await orgs_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        acronym=acronym,
        name=name,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end
    )
