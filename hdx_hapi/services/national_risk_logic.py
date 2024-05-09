from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.national_risk_view_dao import national_risks_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_national_risks_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    risk_class: int = None,
    global_rank: int = None,
    overall_risk: float = None,
    hazard_exposure_risk: float = None,
    vulnerability_risk: float = None,
    coping_capacity_risk: float = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min=None,
    resource_update_date_max=None,
    # sector_name: str = None,
    location_code: str = None,
    location_name: str = None,
):
    return await national_risks_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        risk_class=risk_class,
        global_rank=global_rank,
        overall_risk=overall_risk,
        hazard_exposure_risk=hazard_exposure_risk,
        vulnerability_risk=vulnerability_risk,
        coping_capacity_risk=coping_capacity_risk,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        # sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
    )
