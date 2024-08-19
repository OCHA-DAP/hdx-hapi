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
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def operational_presences_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    sector_code: Optional[str] = None,
    # dataset_hdx_provider_stub: str = None,
    # resource_update_date_min: datetime = None,
    # resource_update_date_max: datetime = None,
    # hapi_updated_date_min: datetime = None,
    # hapi_updated_date_max: datetime = None,
    # hapi_replaced_date_min: datetime = None,
    # hapi_replaced_date_max: datetime = None,
    org_acronym: Optional[str] = None,
    org_name: Optional[str] = None,
    sector_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    location_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Sequence[OperationalPresenceView]:
    logger.info(
        f'operational_presences_view_list called with params: sector_code={sector_code}, '
        f'org_acronym={org_acronym}, org_name={org_name}, '
        f'sector_name={sector_name}, location_code={location_code}, location_name={location_name}, '
        f'admin1_code={admin1_code}, admin1_name={admin1_name}, admin1_is_unspecified={admin1_is_unspecified}, '
        f'admin2_code={admin2_code}, admin2_name={admin2_name}, admin2_is_unspecified={admin2_is_unspecified}, '
        f'ref_period_parameters={ref_period_parameters}'
    )

    query = select(OperationalPresenceView)
    # if dataset_hdx_provider_stub:
    #     query = case_insensitive_filter(
    #         query, OperationalPresenceView.dataset_hdx_provider_stub, dataset_hdx_provider_stub
    #     )
    # if resource_update_date_min:
    #     query = query.where(OperationalPresenceView.resource_update_date >= resource_update_date_min)
    # if resource_update_date_max:
    #     query = query.where(OperationalPresenceView.resource_update_date < resource_update_date_max)
    # if hapi_updated_date_min:
    #     query = query.where(OperationalPresenceView.hapi_updated_date >= hapi_updated_date_min)
    # if hapi_updated_date_max:
    #     query = query.where(OperationalPresenceView.hapi_updated_date < hapi_updated_date_max)
    # if hapi_replaced_date_min:
    #     query = query.where(OperationalPresenceView.hapi_replaced_date >= hapi_replaced_date_min)
    # if hapi_replaced_date_max:
    #     query = query.where(OperationalPresenceView.hapi_replaced_date < hapi_replaced_date_max)
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
        location_ref,
        location_code,
        location_name,
        has_hrp,
        in_gho,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
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
