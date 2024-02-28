import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_population_status_view import PopulationStatusView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter

logger = logging.getLogger(__name__)

async def population_statuses_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):

    logger.info(f'population_statuses_view_list called with params: code={code}, description={description}')

    query = select(PopulationStatusView)
    if code:
        query = case_insensitive_filter(query, PopulationStatusView.code, code)
    if description:
        query = query.where(PopulationStatusView.description.icontains(description))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    population_statuses = result.scalars().all()

    logger.info(f'Retrieved {len(population_statuses)} rows from the database')

    return population_statuses