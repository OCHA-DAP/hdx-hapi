import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import OperationalPresenceView
from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
    case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def operational_presences_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    sector_code: Optional[str] = None,
    org_acronym: Optional[str] = None,
    org_name: Optional[str] = None,
    sector_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[OperationalPresenceView]:
    logger.info(
        f'operational_presences_view_list called with params: sector_code={sector_code}, '
        f'org_acronym={org_acronym}, org_name={org_name}, '
        f'sector_name={sector_name}, location_code={common_location_params.location_code}, '
        f'location_name={common_location_params.location_name}, '
        f'admin1_code={common_location_params.admin1_code}, admin1_name={common_location_params.admin1_name}, '
        f'admin2_code={common_location_params.admin2_code}, admin2_name={common_location_params.admin2_name}, '
        f'ref_period_parameters={ref_period_parameters}, admin_level={common_location_params.admin_level}, '
    )

    query = select(OperationalPresenceView)
    if org_acronym:
        query = case_insensitive_filter(query, OperationalPresenceView.org_acronym, org_acronym)
    if org_name:
        query = query.where(OperationalPresenceView.org_name.icontains(org_name))
    if sector_code:
        query = query.where(OperationalPresenceView.sector_code.icontains(sector_code))
    if sector_name:
        query = query.where(OperationalPresenceView.sector_name.icontains(sector_name))

    query = apply_location_admin_filter(
        query,
        OperationalPresenceView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, OperationalPresenceView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        OperationalPresenceView.admin2_ref,
        OperationalPresenceView.org_acronym,
        OperationalPresenceView.org_name,
        OperationalPresenceView.sector_code,
        OperationalPresenceView.reference_period_start,
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    operational_presences = result.scalars().all()

    logger.info(f'Retrieved {len(operational_presences)} rows from the database')

    return operational_presences
