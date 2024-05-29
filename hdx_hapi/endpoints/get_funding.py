from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Query

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import DOC_LOCATION_CODE, DOC_LOCATION_NAME, DOC_SEE_LOC
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.funding import FundingResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.funding_logic import get_funding_srv
from hdx_hapi.services.sql_alchemy_session import get_db


router = APIRouter(
    tags=['Coordination & Context'],
)


@router.get(
    '/api/coordination-context/funding',
    response_model=HapiGenericResponse[FundingResponse],
    summary='Get funding data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/coordination-context/funding',
    response_model=HapiGenericResponse[FundingResponse],
    summary='Get funding data',
)
async def get_fundings(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    appeal_code: Annotated[Optional[str], Query(max_length=32, description='Appeal code')] = None,
    appeal_type: Annotated[Optional[str], Query(max_length=32, description='Appeal type')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_funding_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        appeal_code=appeal_code,
        appeal_type=appeal_type,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, FundingResponse)
