from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_dataset_view import DatasetView
from hdx_hapi.db.dao.util.util import apply_pagination

async def datasets_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    title: str = None,
    provider_code: str = None,
    provider_name: str = None,
):

    query = select(DatasetView)
    if code:
        query = query.where(DatasetView.code == code)
    if title:
        query = query.where(DatasetView.title == title)
    if provider_code:
        query = query.where(DatasetView.provider_code == provider_code)
    if provider_name:
        query = query.where(DatasetView.provider_name == provider_name)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    datasets = result.scalars().all()
    return datasets