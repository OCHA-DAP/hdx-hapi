from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
from hapi_schema.utils.enums import RiskClass


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_NAME,
    DOC_RISK_CLASS,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.national_risk import NationalRiskResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.national_risk_logic import get_national_risks_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

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
async def get_national_risk(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    risk_class: Annotated[Optional[RiskClass], Query(description=DOC_RISK_CLASS)] = None,
    global_rank_min: Annotated[
        Optional[int], Query(description='Filter the response by a lower bound for the Global Rank.')
    ] = None,
    global_rank_max: Annotated[
        Optional[int], Query(description='Filter the response by an upper bound for the Global Rank.')
    ] = None,
    overall_risk_min: Annotated[
        Optional[float], Query(description='Filter the response by a lower bound for the Overall Risk.')
    ] = None,
    overall_risk_max: Annotated[
        Optional[float], Query(description='Filter the response by an upper bound for the Overall Risk.')
    ] = None,
    hazard_exposure_risk_min: Annotated[
        Optional[float], Query(description='Filter the response by a lower bound for the Hazard Exposure Risk.')
    ] = None,
    hazard_exposure_risk_max: Annotated[
        Optional[float], Query(description='Filter the response by an upper bound for the Hazard Exposure Risk.')
    ] = None,
    vulnerability_risk_min: Annotated[
        Optional[float], Query(description='Filter the response by a lower bound for the Vulnerability Risk.')
    ] = None,
    vulnerability_risk_max: Annotated[
        Optional[float], Query(description='Filter the response by an upper bound for the Vulnerability Risk.')
    ] = None,
    coping_capacity_risk_min: Annotated[
        Optional[float], Query(description='Filter the response by a lower bound for the Coping Capacity Risk.')
    ] = None,
    coping_capacity_risk_max: Annotated[
        Optional[float], Query(description='Filter the response by a lower bound for the Coping Capacity Risk.')
    ] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
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
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, NationalRiskResponse)


get_national_risk.__doc__ = (
    'European Commission national risk data from the INFORM-risk framework. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'coordination_and_context/#national-risk">HDX HAPI documentation</a>, '
    'and the <a href="https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk">'
    'original INFORM-risk source</a> website.'
)
