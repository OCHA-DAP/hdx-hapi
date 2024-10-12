from typing import Optional

from hapi_schema.utils.enums import RiskClass
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.national_risk_view_dao import national_risks_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_national_risks_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
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
    return await national_risks_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        risk_class=risk_class,
        global_rank_min=global_rank_min,
        global_rank_max=global_rank_max,
        overall_risk_min=overall_risk_min,
        overall_risk_max=overall_risk_max,
        hazard_exposure_risk_min=hazard_exposure_risk_min,
        hazard_exposure_risk_max=hazard_exposure_risk_max,
        vulnerability_risk_min=vulnerability_risk_min,
        vulnerability_risk_max=vulnerability_risk_max,
        coping_capacity_risk_min=coping_capacity_risk_min,
        coping_capacity_risk_max=coping_capacity_risk_max,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
