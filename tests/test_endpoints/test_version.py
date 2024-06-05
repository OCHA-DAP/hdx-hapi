import pytest
import logging

from httpx import AsyncClient
from main import app
from hdx_hapi.endpoints.util import version as hapi_version

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v1/util/version'


@pytest.mark.asyncio
async def test_version():
    log.info('started test_version')

    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()) == 2, 'Response has a different number of fields than expected'
    assert response.json() == {
        'api_version': hapi_version.api_version,
        'hapi_sqlalchemy_schema_version': hapi_version.hapi_sqlalchemy_schema_version,
    }
