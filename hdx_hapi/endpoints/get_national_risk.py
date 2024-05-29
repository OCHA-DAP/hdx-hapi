from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
from hapi_schema.utils.enums import RiskClass


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.national_risk import NationalRiskResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    ReferencePeriodParameters,
    common_endpoint_parameters,
    reference_period_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.national_risk_logic import get_national_risks_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Coordination & Context'],
)


@router.get(
    '/api/coordination-context/national-risk',
    response_model=HapiGenericResponse[NationalRiskResponse],
    summary='Get national risk data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/coordination-context/national-risk',
    response_model=HapiGenericResponse[NationalRiskResponse],
    summary='Get national risk data',
)
async def get_national_risks(
    ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    risk_class: Annotated[Optional[RiskClass], Query(description='Risk class')] = None,
    global_rank_min: Annotated[Optional[int], Query(description='Global rank, lower bound')] = None,
    global_rank_max: Annotated[Optional[int], Query(description='Global rank, upper bound')] = None,
    overall_risk_min: Annotated[Optional[float], Query(description='Overall risk, lower bound')] = None,
    overall_risk_max: Annotated[Optional[float], Query(description='Overall risk, upper bound')] = None,
    hazard_exposure_risk_min: Annotated[Optional[float], Query(description='Hazard exposure risk, lower bound')] = None,
    hazard_exposure_risk_max: Annotated[Optional[float], Query(description='Hazard exposure risk, upper bound')] = None,
    vulnerability_risk_min: Annotated[Optional[float], Query(description='Vulnerability risk, lower bound')] = None,
    vulnerability_risk_max: Annotated[Optional[float], Query(description='Vulnerability risk, upper bound')] = None,
    coping_capacity_risk_min: Annotated[Optional[float], Query(description='Coping capacity risk, lower bound')] = None,
    coping_capacity_risk_max: Annotated[Optional[float], Query(description='Coping capacity risk, upper bound')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of national risks
    """
    result = await get_national_risks_srv(
        pagination_parameters=common_parameters,
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
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, NationalRiskResponse)
