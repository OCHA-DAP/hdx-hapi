import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_dataset_view import DatasetView
from hdx_hapi.db.dao.util.util import apply_pagination

logger = logging.getLogger(__name__)

async def datasets_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    hdx_id: str = None,
    hdx_stub: str = None,
    title: str = None,
    provider_code: str = None,
    provider_name: str = None,
):

    logger.info(f'datasets_view_list called with params: hdx_id={hdx_id}, hdx_stub={hdx_stub}, title={title}, provider_code={provider_code}, provider_name={provider_name}')

    query = select(DatasetView)
    if hdx_id:
        query = query.where(DatasetView.hdx_id == hdx_id)
    if hdx_stub:
        query = query.where(DatasetView.hdx_stub == hdx_stub)
    if title:
        query = query.where(DatasetView.title.icontains(title))
    if provider_code:
        query = query.where(DatasetView.provider_code == provider_code)
    if provider_name:
        query = query.where(DatasetView.provider_name.icontains(provider_name))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    datasets = result.scalars().all()

    logger.info(f'Retrieved {len(datasets)} rows from the database')

    return datasets