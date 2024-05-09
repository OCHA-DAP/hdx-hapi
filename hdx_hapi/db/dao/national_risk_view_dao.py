import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_national_risk_view import NationalRiskView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


async def national_risks_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    risk_class: int = None,
    global_rank: int = None,
    overall_risk: float = None,
    hazard_exposure_risk: float = None,
    vulnerability_risk: float = None,
    coping_capacity_risk: float = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    # sector_name: str = None,
    location_code: str = None,
    location_name: str = None,
):
    query = select(NationalRiskView)
    if risk_class:
        query = query.where(NationalRiskView.risk_class == risk_class)
    if global_rank:
        query = query.where(NationalRiskView.global_rank == global_rank)
    if overall_risk:
        query = query.where(NationalRiskView.overall_risk == overall_risk)
    if hazard_exposure_risk:
        query = query.where(NationalRiskView.hazard_exposure_risk == hazard_exposure_risk)
    if vulnerability_risk:
        query = query.where(NationalRiskView.vulnerability_risk == vulnerability_risk)
    if coping_capacity_risk:
        query = query.where(NationalRiskView.coping_capacity_risk == coping_capacity_risk)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(query, NationalRiskView.dataset_hdx_provider_stub, dataset_hdx_provider_stub)
    if resource_update_date_min:
        query = query.where(NationalRiskView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(NationalRiskView.resource_update_date < resource_update_date_max)
    # if sector_name:
    # query = query.where(NationalRiskView.sector_name.icontains(sector_name))
    if location_code:
        query = case_insensitive_filter(query, NationalRiskView.location_code, location_code)
    if location_name:
        query = query.where(NationalRiskView.location_name.icontains(location_name))

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    national_risks = result.scalars().all()
    return national_risks
