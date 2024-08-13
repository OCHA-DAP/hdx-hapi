import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import CurrencyView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def currencies_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
):
    logger.info(f'currency_view_list called with params: code={code}')

    query = select(CurrencyView)
    if code:
        query = case_insensitive_filter(query, CurrencyView.code, code)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(CurrencyView.code.asc())

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    currencies = result.scalars().all()

    logger.info(f'Retrieved {len(currencies)} rows from the database')

    return currencies
