# import base64
import pytest
import logging

from httpx import AsyncClient
from main import app
# from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER_LIST = [
    '/api/v1/metadata/admin1',
    '/api/v1/metadata/admin2',
    '/api/v1/metadata/dataset',
    '/api/v1/affected-people/humanitarian-needs',
    '/api/v1/metadata/location',
    '/api/v1/metadata/org',
    '/api/v1/metadata/org_type',
    '/api/v1/metadata/resource',
    '/api/v1/metadata/sector',
    # TODO to fix the following endpoints
    '/api/v1/themes/food_security',
    '/api/v1/themes/national_risk',
    '/api/v1/themes/3W',
    '/api/v1/themes/population',
    '/api/v1/population_group',
    '/api/v1/population_status',
]


APP_IDENTIFIER = 'aGFwaV90ZXN0OmhhcGlAaHVtZGF0YS5vcmc='
query_parameters = {'app_identifier': APP_IDENTIFIER}


@pytest.mark.asyncio
async def test_endpoints_vs_encode_identifier(event_loop, refresh_db, enable_hapi_identifier_filtering):
    log.info('started test_endpoints_vs_encode_identifier')

    for endpoint_router in ENDPOINT_ROUTER_LIST:
        async with AsyncClient(app=app, base_url='http://test') as ac:
            response = await ac.get(endpoint_router)
        assert response.status_code == 400

        async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
            response = await ac.get(endpoint_router)
        assert response.status_code == 400
        response_items = response.json()
        assert len(response_items) > 0


@pytest.mark.asyncio
async def test_encode_identifier(event_loop, refresh_db, enable_hapi_identifier_filtering):
    # testing the encode identifier endpoint
    endpoint_router = '/api/v1/encode_identifier'

    # it should not be important if app_identifier is passed or not to the endpoint
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 422

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 422
