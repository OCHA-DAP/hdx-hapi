import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_dataset_view import DatasetView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def datasets_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    hdx_id: str = None,
    hdx_stub: str = None,
    title: str = None,
    hdx_provider_stub: str = None,
    hdx_provider_name: str = None,
):
    logger.info(
        f'datasets_view_list called with params: hdx_id={hdx_id}, hdx_stub={hdx_stub}, title={title}, '
        f'hdx_provider_stub={hdx_provider_stub}, hdx_provider_name={hdx_provider_name}'
    )

    query = select(DatasetView)
    if hdx_id:
        query = query.where(DatasetView.hdx_id == hdx_id)
    if hdx_stub:
        query = query.where(DatasetView.hdx_stub == hdx_stub)
    if title:
        query = query.where(DatasetView.title.icontains(title))
    if hdx_provider_stub:
        query = case_insensitive_filter(query, DatasetView.hdx_provider_stub, hdx_provider_stub)
    if hdx_provider_name:
        query = query.where(DatasetView.hdx_provider_name.icontains(hdx_provider_name))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    datasets = result.scalars().all()

    logger.info(f'Retrieved {len(datasets)} rows from the database')

    return datasets
