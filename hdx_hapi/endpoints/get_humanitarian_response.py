from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_ORG_ACRONYM,
    DOC_ORG_NAME,
    DOC_ORG_TYPE_CODE,
    DOC_ORG_TYPE_DESCRIPTION,
    DOC_SECTOR_CODE,
    DOC_SECTOR_NAME,
    DOC_SEE_ORG_TYPE
)

from hdx_hapi.endpoints.models.humanitarian_response import OrgResponse, OrgTypeResponse, SectorResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.org_logic import get_orgs_srv
from hdx_hapi.services.org_type_logic import get_org_types_srv
from hdx_hapi.services.sector_logic import get_sectors_srv
from hdx_hapi.services.sql_alchemy_session import get_db


router = APIRouter(
    tags=['Humanitarian Organizations and Sectors'],
)

@router.get('/api/org', response_model=List[OrgResponse],
            summary='Get the list of organizations represented in the data available in HAPI')
async def get_orgs(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    acronym: Annotated[str, Query(max_length=32, description=f'{DOC_ORG_ACRONYM}', example='unhcr')] = None,
    name: Annotated[
        str,
        Query(max_length=512, description=f'{DOC_ORG_NAME}', example='United Nations High Commissioner for Refugees')
    ] = None,
    org_type_code: Annotated[str, Query(max_length=32, description=f'{DOC_ORG_TYPE_CODE}')] = None,
    org_type_description: Annotated[
        str, 
        Query(max_length=512, description=f'{DOC_ORG_TYPE_DESCRIPTION} {DOC_SEE_ORG_TYPE}')
    ] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    """    
    result = await get_orgs_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        acronym=acronym,
        name=name,
        org_type_code=org_type_code,
        org_type_description=org_type_description
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, OrgResponse)

@router.get('/api/org_type', response_model=List[OrgTypeResponse],
            summary='Get information about how organizations are classified in HAPI')
async def get_org_types(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description=f'{DOC_ORG_TYPE_CODE}', example='433')] = None,
    description: Annotated[
        str,
        Query(max_length=512, description=f'{DOC_ORG_TYPE_DESCRIPTION}', example='Donor')
    ] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """There is no agreed standard for the classification of organizations. The codes and descriptions used in HAPI are 
    based on <a href="https://data.humdata.org/dataset/organization-types-beta">this dataset</a>.
    """    
    result = await get_org_types_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, OrgTypeResponse)

@router.get('/api/sector', response_model=List[SectorResponse],
            summary='Get information about how humanitarian response activities are classified')
async def get_sectors(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description=f'{DOC_SECTOR_CODE}', example='hea')] = None,
    name: Annotated[str, Query(max_length=512, description=f'{DOC_SECTOR_NAME}', example='Health')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """There is no consistent standard for the humanitarian sectors. The codes and descriptions used in HAPI are based 
    on <a href="https://data.humdata.org/organization/54255d0b-c6b1-4517-9722-17321f6634ab">this dataset</a>.
    """    
    result = await get_sectors_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, SectorResponse)
