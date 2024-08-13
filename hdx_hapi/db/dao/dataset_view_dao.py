import logging
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import DatasetView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def datasets_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    dataset_hdx_id: Optional[str] = None,
    dataset_hdx_stub: Optional[str] = None,
    dataset_hdx_title: Optional[str] = None,
    hdx_provider_stub: Optional[str] = None,
    hdx_provider_name: Optional[str] = None,
):
    logger.info(
        f'datasets_view_list called with params: dataset_hdx_id={dataset_hdx_id}, dataset_hdx_stub={dataset_hdx_stub}, '
        f'dataset_hdx_title={dataset_hdx_title}, hdx_provider_stub={hdx_provider_stub}, '
        f'hdx_provider_name={hdx_provider_name}'
    )

    query = select(DatasetView)
    if dataset_hdx_id:
        query = query.where(DatasetView.dataset_hdx_id == dataset_hdx_id)
    if dataset_hdx_stub:
        query = query.where(DatasetView.dataset_hdx_stub == dataset_hdx_stub)
    if dataset_hdx_title:
        query = query.where(DatasetView.dataset_hdx_title.icontains(dataset_hdx_title))
    if hdx_provider_stub:
        query = case_insensitive_filter(query, DatasetView.hdx_provider_stub, hdx_provider_stub)
    if hdx_provider_name:
        query = query.where(DatasetView.hdx_provider_name.icontains(hdx_provider_name))

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(DatasetView.dataset_hdx_stub.asc())

    logger.info(f'Executing SQL query: {query}')

    result = await db.execute(query)
    datasets = result.scalars().all()

    logger.info(f'Retrieved {len(datasets)} rows from the database')

    return datasets
