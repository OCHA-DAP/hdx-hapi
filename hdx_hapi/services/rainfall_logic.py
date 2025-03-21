from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import AggregationPeriod

from hdx_hapi.db.dao.rainfall_view_dao import rainfall_view_list
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    ReferencePeriodParameters,
)


async def get_rainfall_srv(
    common_date_range_params: CommonDateRangeParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    pagination_parameters: CommonEndpointParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    aggregation_period: Optional[AggregationPeriod] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    return await rainfall_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        aggregation_period=aggregation_period,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
