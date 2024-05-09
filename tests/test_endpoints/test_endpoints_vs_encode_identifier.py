# import base64
import pytest
import logging

from httpx import AsyncClient
from main import app
# from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER_LIST = [
    '/api/v1/admin1',
    '/api/v1/admin2',
    '/api/v1/dataset',
    '/api/v1/themes/food_security',
    '/api/v1/themes/humanitarian_needs',
    '/api/v1/location',
    '/api/v1/themes/national_risk',
    '/api/v1/themes/3W',
    '/api/v1/org',
    '/api/v1/org_type',
    '/api/v1/themes/population',
    '/api/v1/population_group',
    '/api/v1/population_status',
    '/api/v1/resource',
    '/api/v1/sector',
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
        assert response.status_code == 200
        response_items = response.json()
        assert len(response_items) > 0


@pytest.mark.asyncio
async def test_encode_identifier(event_loop, refresh_db, enable_hapi_identifier_filtering):
    # testing the encode identifier endpoint
    endpoint_router = '/api/v1/encode_identifier'

    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 200
    response_items = response.json()
    assert len(response_items) > 0
