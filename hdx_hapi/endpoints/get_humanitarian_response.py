from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_ORG_ACRONYM,
    DOC_ORG_NAME,
    DOC_ORG_TYPE_CODE,
    DOC_ORG_TYPE_DESCRIPTION,
    DOC_SECTOR_CODE,
    DOC_SECTOR_NAME,
    DOC_SEE_ORG_TYPE,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.humanitarian_response import OrgResponse, OrgTypeResponse, SectorResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested

from hdx_hapi.services.org_logic import get_orgs_srv
from hdx_hapi.services.org_type_logic import get_org_types_srv
from hdx_hapi.services.sector_logic import get_sectors_srv
from hdx_hapi.services.sql_alchemy_session import get_db


router = APIRouter(
    tags=['Metadata'],
)


@router.get(
    '/api/metadata/org',
    response_model=HapiGenericResponse[OrgResponse],
    summary='Get the list of organizations represented in the data available in HDX HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/org',
    response_model=HapiGenericResponse[OrgResponse],
    summary='Get the list of organizations represented in the data available in HDX HAPI',
)
async def get_org(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    acronym: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_ORG_ACRONYM}')] = None,
    name: Annotated[
        Optional[str],
        Query(
            max_length=512,
            description=f'{DOC_ORG_NAME}',
        ),
    ] = None,
    org_type_code: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_ORG_TYPE_CODE}')] = None,
    org_type_description: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ORG_TYPE_DESCRIPTION} {DOC_SEE_ORG_TYPE}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """ """
    result = await get_orgs_srv(
        pagination_parameters=common_parameters,
        db=db,
        acronym=acronym,
        name=name,
        org_type_code=org_type_code,
        org_type_description=org_type_description,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, OrgResponse)


@router.get(
    '/api/metadata/org_type',
    response_model=HapiGenericResponse[OrgTypeResponse],
    summary='Get information about how organizations are classified in HDX HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/org-type',
    response_model=HapiGenericResponse[OrgTypeResponse],
    summary='Get information about how organizations are classified in HDX HAPI',
)
async def get_org_type(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_ORG_TYPE_CODE}')] = None,
    description: Annotated[
        Optional[str],
        Query(max_length=512, description=f'{DOC_ORG_TYPE_DESCRIPTION}'),
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """There is no agreed standard for the classification of organizations. The codes and descriptions used in HDX HAPI
    are based on <a href="https://data.humdata.org/dataset/organization-types-beta">this dataset</a>.
    """
    result = await get_org_types_srv(pagination_parameters=common_parameters, db=db, code=code, description=description)
    return transform_result_to_csv_stream_if_requested(result, output_format, OrgTypeResponse)


@router.get(
    '/api/metadata/sector',
    response_model=HapiGenericResponse[SectorResponse],
    summary='Get information about how humanitarian response activities are classified',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/sector',
    response_model=HapiGenericResponse[SectorResponse],
    summary='Get information about how humanitarian response activities are classified',
)
async def get_sector(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_SECTOR_CODE}')] = None,
    name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """There are a variety of standards for the naming of humanitarian sectors. The codes and descriptions used
    in HDX HAPI are based on
    <a href="https://data.humdata.org/organization/54255d0b-c6b1-4517-9722-17321f6634ab">this dataset</a>.
    """
    result = await get_sectors_srv(
        pagination_parameters=common_parameters,
        db=db,
        code=code,
        name=name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, SectorResponse)
