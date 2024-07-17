from typing import Optional

from hapi_schema.utils.enums import RiskClass
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import NationalRiskView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def national_risks_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    risk_class: Optional[RiskClass] = None,
    global_rank_min: Optional[int] = None,
    global_rank_max: Optional[int] = None,
    overall_risk_min: Optional[float] = None,
    overall_risk_max: Optional[float] = None,
    hazard_exposure_risk_min: Optional[float] = None,
    hazard_exposure_risk_max: Optional[float] = None,
    vulnerability_risk_min: Optional[float] = None,
    vulnerability_risk_max: Optional[float] = None,
    coping_capacity_risk_min: Optional[float] = None,
    coping_capacity_risk_max: Optional[float] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    query = select(NationalRiskView)
    if risk_class:
        query = query.where(NationalRiskView.risk_class == risk_class)
    if global_rank_min:
        query = query.where(NationalRiskView.global_rank >= global_rank_min)
    if global_rank_max:
        query = query.where(NationalRiskView.global_rank < global_rank_max)
    if overall_risk_min:
        query = query.where(NationalRiskView.overall_risk >= overall_risk_min)
    if overall_risk_max:
        query = query.where(NationalRiskView.overall_risk < overall_risk_max)
    if hazard_exposure_risk_min:
        query = query.where(NationalRiskView.hazard_exposure_risk >= hazard_exposure_risk_min)
    if hazard_exposure_risk_max:
        query = query.where(NationalRiskView.hazard_exposure_risk < hazard_exposure_risk_max)
    if vulnerability_risk_min:
        query = query.where(NationalRiskView.vulnerability_risk >= vulnerability_risk_min)
    if vulnerability_risk_max:
        query = query.where(NationalRiskView.vulnerability_risk < vulnerability_risk_max)
    if coping_capacity_risk_min:
        query = query.where(NationalRiskView.coping_capacity_risk >= coping_capacity_risk_min)
    if coping_capacity_risk_max:
        query = query.where(NationalRiskView.coping_capacity_risk < coping_capacity_risk_max)

    if has_hrp:
        query = query.where(NationalRiskView.has_hrp == has_hrp)
    if in_gho:
        query = query.where(NationalRiskView.in_gho == in_gho)

    # if sector_name:
    # query = query.where(NationalRiskView.sector_name.icontains(sector_name))
    if location_code:
        query = case_insensitive_filter(query, NationalRiskView.location_code, location_code)
    if location_name:
        query = query.where(NationalRiskView.location_name.icontains(location_name))

    query = apply_reference_period_filter(query, ref_period_parameters, NationalRiskView)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    national_risks = result.scalars().all()
    return national_risks
