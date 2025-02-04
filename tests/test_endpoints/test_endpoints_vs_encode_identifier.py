# import base64
import pytest
import logging

from httpx import ASGITransport, AsyncClient
from main import app
# from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER_LIST = [
    '/api/v1/affected-people/refugees',
    '/api/v1/affected-people/humanitarian-needs',
    '/api/v1/coordination-context/operational-presence',
    '/api/v1/coordination-context/funding',
    '/api/v1/coordination-context/conflict-event',
    '/api/v1/coordination-context/national-risk',
    '/api/v1/food/food-security',
    '/api/v1/food/food-price',
    '/api/v1/population-social/population',
    '/api/v1/population-social/poverty-rate',
    '/api/v1/metadata/dataset',
    '/api/v1/metadata/resource',
    '/api/v1/metadata/location',
    '/api/v1/metadata/admin1',
    '/api/v1/metadata/admin2',
    '/api/v1/metadata/org',
    '/api/v1/metadata/org-type',
    '/api/v1/metadata/sector',
    '/api/v1/metadata/currency',
    '/api/v1/metadata/wfp-commodity',
    '/api/v1/metadata/wfp-market',
    '/api/v1/metadata/data-availability',
    '/api/v2/food-security-nutrition-poverty/food-prices-market-monitor',
    '/api/v2/food-security-nutrition-poverty/food-security',
    '/api/v2/food-security-nutrition-poverty/poverty-rate',
    '/api/v2/geography-infrastructure/baseline-population',
    '/api/v2/coordination-context/national-risk',
    '/api/v2/coordination-context/conflict-event',
    '/api/v2/coordination-context/funding',
    '/api/v2/coordination-context/operational-presence',
    '/api/v2/affected-people/humanitarian-needs',
    '/api/v2/affected-people/refugees-persons-of-concern',
    '/api/v2/affected-people/returnees',
    '/api/v2/metadata/location',
    '/api/v2/metadata/dataset',
    '/api/v2/metadata/resource',
    '/api/v2/metadata/admin1',
    '/api/v2/metadata/admin2',
    '/api/v2/metadata/org',
    '/api/v2/metadata/org-type',
    '/api/v2/metadata/sector',
    '/api/v2/metadata/currency',
    '/api/v2/metadata/wfp-commodity',
    '/api/v2/metadata/wfp-market',
    '/api/v2/metadata/data-availability',
]

APP_IDENTIFIER = 'aGFwaV90ZXN0OmhhcGlAaHVtZGF0YS5vcmc='
query_parameters = {'app_identifier': APP_IDENTIFIER}


@pytest.mark.asyncio
async def test_endpoints_vs_encode_identifier(event_loop, refresh_db, enable_hapi_identifier_filtering):
    log.info('started test_endpoints_vs_encode_identifier')

    for endpoint_router in ENDPOINT_ROUTER_LIST:
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get(endpoint_router)
        assert response.status_code == 403

        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
            response = await ac.get(endpoint_router)
        assert response.status_code == 200
        response_items = response.json()
        assert len(response_items) > 0


@pytest.mark.asyncio
async def test_encode_identifier(event_loop, refresh_db, enable_hapi_identifier_filtering):
    # testing the encode identifier endpoint
    endpoint_router = '/api/v2/encode_app_identifier'

    # it should not be important if app_identifier is passed or not to the endpoint
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 422

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 422
