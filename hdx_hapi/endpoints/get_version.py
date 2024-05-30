from fastapi import APIRouter

from hdx_hapi.endpoints.models.version import VersionResponse
from hdx_hapi.endpoints.util import version as hapi_version

router = APIRouter(
    tags=['Util'],
)

SUMMARY_TEXT = 'Display the API and SQL Alchemy versions'


@router.get(
    '/api/util/version',
    response_model=VersionResponse,
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/util/version',
    response_model=VersionResponse,
    summary=SUMMARY_TEXT,
)
async def get_version():
    result = {
        'api_version': hapi_version.api_version,
        'hapi_sqlalchemy_schema_version': hapi_version.hapi_sqlalchemy_schema_version,
    }
    return result
