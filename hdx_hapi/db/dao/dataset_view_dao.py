import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import DatasetView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def datasets_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    dataset_hdx_id: str = None,
    hdx_stub: str = None,
    title: str = None,
    hdx_provider_stub: str = None,
    hdx_provider_name: str = None,
):
    logger.info(
        f'datasets_view_list called with params: dataset_hdx_id={dataset_hdx_id}, dataset_hdx_stub={hdx_stub}, '
        f'title={title}, '
        f'hdx_provider_stub={hdx_provider_stub}, hdx_provider_name={hdx_provider_name}'
    )

    query = select(DatasetView)
    # query = select(
    #     (
    #         DatasetView.hdx_id,
    #         DatasetView.hdx_stub,
    #         DatasetView.title,
    #         DatasetView.hdx_provider_stub,
    #         DatasetView.hdx_provider_name,
    #     )
    # )
    if dataset_hdx_id:
        query = query.where(DatasetView.hdx_id == dataset_hdx_id)
    if hdx_stub:
        query = query.where(DatasetView.hdx_stub == hdx_stub)
    if title:
        query = query.where(DatasetView.title.icontains(title))
    if hdx_provider_stub:
        query = case_insensitive_filter(query, DatasetView.hdx_provider_stub, hdx_provider_stub)
    if hdx_provider_name:
        query = query.where(DatasetView.hdx_provider_name.icontains(hdx_provider_name))

    query = apply_pagination(query, pagination_parameters)

    logger.info(f'Executing SQL query: {query}')

    result = await db.execute(query)
    datasets = result.scalars().all()

    logger.info(f'Retrieved {len(datasets)} rows from the database')
    for row in datasets:
        print(row, flush=True)

    return datasets
