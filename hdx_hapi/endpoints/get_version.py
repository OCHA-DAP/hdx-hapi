from fastapi import APIRouter

from hdx_hapi.endpoints.models.version import VersionResponse
from hdx_hapi.endpoints.util import version as hapi_version

router = APIRouter(
    tags=['Util'],
)


SUMMARY_TEXT = 'Display the API and SQL Alchemy versions'

ROUTER_DICT = {
    'response_model': VersionResponse,
    'summary': SUMMARY_TEXT,
}


@router.get('/api/util/version', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/util/version', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/util/version', **ROUTER_DICT)
async def get_version():
    result = {
        'api_version': hapi_version.api_version,
        'hapi_sqlalchemy_schema_version': hapi_version.hapi_sqlalchemy_schema_version,
    }
    return result
