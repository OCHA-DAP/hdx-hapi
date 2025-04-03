import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hapi_schema.utils.enums import AggregationPeriod, Version

from hdx_hapi.db.models.views.vat_or_view import RainfallView
from hdx_hapi.db.dao.util.util import (
    apply_date_range_filter,
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
    # case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)


logger = logging.getLogger(__name__)


async def rainfall_view_list(
    pagination_parameters: PaginationParams,
    common_date_range_params: CommonDateRangeParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    aggregation_period: Optional[AggregationPeriod] = None,
    version: Optional[Version] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[RainfallView]:
    logger.info(
        f'rainfall_view_list called with params: aggregation_period={aggregation_period} '
        f'location_name={common_location_params.location_name}, '
        f'admin1_code={common_location_params.admin1_code}, admin1_name={common_location_params.admin1_name}, '
        f'admin2_code={common_location_params.admin2_code}, admin2_name={common_location_params.admin2_name}, '
        f'ref_period_parameters={ref_period_parameters}, admin_level={common_location_params.admin_level}, '
    )

    query = select(RainfallView)
    if aggregation_period:
        query = query.where(RainfallView.aggregation_period == aggregation_period)

    if version:
        query = query.where(RainfallView.version == version)

    query = apply_date_range_filter(
        query,
        RainfallView,
        common_date_range_params,
    )

    query = apply_location_admin_filter(
        query,
        RainfallView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, RainfallView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(RainfallView.admin2_ref, RainfallView.aggregation_period)

    logger.info(f'Executing SQL query: {query}')

    result = await db.execute(query)
    rainfall = result.scalars().all()

    logger.info(f'Retrieved {len(rainfall)} rows from the database')

    return rainfall
