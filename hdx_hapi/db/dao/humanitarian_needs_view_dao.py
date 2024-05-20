import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import HumanitarianNeedsView
from hdx_hapi.db.dao.util.util import apply_location_admin_filter, apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


async def humanitarian_needs_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    gender_code: str = None,
    age_range_code: str = None,
    disabled_marker: bool = None,
    sector_code: str = None,
    sector_name: str = None,
    population_group_code: str = None,
    population_status_code: str = None,
    population: int = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    admin1_is_unspecified: bool = None,
    location_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
    admin1_ref: int = None,
    admin2_ref: int = None,
):
    query = select(HumanitarianNeedsView)

    if gender_code:
        query = case_insensitive_filter(query, HumanitarianNeedsView.gender_code, gender_code)
    if age_range_code:
        query = query.where(HumanitarianNeedsView.age_range_code == age_range_code)
    if disabled_marker:
        query = query.where(HumanitarianNeedsView.disabled_marker == disabled_marker)
    if sector_code:
        query = query.where(HumanitarianNeedsView.sector_code.icontains(sector_code))
    if sector_name:
        query = query.where(HumanitarianNeedsView.sector_name.icontains(sector_name))
    if population_group_code:
        query = query.where(HumanitarianNeedsView.population_group_code.icontains(population_group_code))
    if population_status_code:
        query = query.where(HumanitarianNeedsView.population_status_code.icontains(population_status_code))
    if population:
        query = query.where(HumanitarianNeedsView.population == population)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(
            query, HumanitarianNeedsView.dataset_hdx_provider_stub, dataset_hdx_provider_stub
        )
    if resource_update_date_min:
        query = query.where(HumanitarianNeedsView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(HumanitarianNeedsView.resource_update_date < resource_update_date_max)
    if hapi_updated_date_min:
        query = query.where(HumanitarianNeedsView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(HumanitarianNeedsView.hapi_updated_date < hapi_updated_date_max)
    if hapi_replaced_date_min:
        query = query.where(HumanitarianNeedsView.hapi_replaced_date >= hapi_replaced_date_min)
    if hapi_replaced_date_max:
        query = query.where(HumanitarianNeedsView.hapi_replaced_date < hapi_replaced_date_max)

    query = apply_location_admin_filter(
        query,
        HumanitarianNeedsView,
        location_ref,
        location_code,
        location_name,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    humanitarian_needs = result.scalars().all()
    return humanitarian_needs
