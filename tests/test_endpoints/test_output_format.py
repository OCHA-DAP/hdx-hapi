import pytest
import logging
import csv
from httpx import ASGITransport, AsyncClient
from main import app

log = logging.getLogger(__name__)

# ENDPOINT_ROUTER = '/api/admin1'
# endpoint_data = endpoint_data[ENDPOINT_ROUTER]
# query_parameters = endpoint_data['query_parameters']
# expected_fields = endpoint_data['expected_fields']
ENDPOINT_ROUTER_LIST = [
    '/api/v1/metadata/admin1',
    '/api/v1/metadata/admin2',
    '/api/v1/metadata/dataset',
    '/api/v1/affected-people/humanitarian-needs',
    '/api/v1/metadata/location',
    '/api/v1/metadata/org',
    '/api/v1/metadata/org-type',
    '/api/v1/metadata/resource',
    '/api/v1/metadata/sector',
    '/api/v1/population-social/population',
    '/api/v1/population-social/poverty-rate',
    '/api/v1/coordination-context/national-risk',
    '/api/v1/coordination-context/operational-presence',
    '/api/v1/affected-people/refugees',
    '/api/v1/affected-people/returnees',
    '/api/v1/affected-people/idps',
    '/api/v1/coordination-context/funding',
    '/api/v1/coordination-context/conflict-event',
    '/api/v1/food/food-security',
    '/api/v1/metadata/currency',
    '/api/v2/food-security-nutrition-poverty/food-prices-market-monitor',
    '/api/v2/food-security-nutrition-poverty/food-security',
    '/api/v2/food-security-nutrition-poverty/poverty-rate',
    '/api/v2/coordination-context/national-risk',
    '/api/v2/coordination-context/operational-presence',
    '/api/v2/affected-people/humanitarian-needs',
    '/api/v2/affected-people/refugees-persons-of-concern',
    '/api/v2/affected-people/returnees',
    'api/v2/affected-people/idps',
    '/api/v2/metadata/location',
    '/api/v2/metadata/admin1',
    '/api/v2/metadata/admin2',
    '/api/v2/metadata/dataset',
    '/api/v2/metadata/location',
    '/api/v2/metadata/org',
    '/api/v2/metadata/org-type',
    '/api/v2/metadata/resource',
    '/api/v2/metadata/sector',
    '/api/v2/metadata/currency',
    '/api/v1/coordination-context/conflict-events',
]


@pytest.mark.parametrize('endpoint_router', ENDPOINT_ROUTER_LIST)
@pytest.mark.asyncio
async def test_output_format(event_loop, refresh_db, endpoint_router):
    log.info('started ' + endpoint_router)
    # JSON by default
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json', 'The output should be in json format'
    no_rows_json = len(response.json()['data'])
    assert no_rows_json > 0

    # CSV
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='http://test', params={'output_format': 'csv'}
    ) as ac:
        response = await ac.get(endpoint_router)
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'text/csv; charset=utf-8', 'The output should be in csv format'
    csv_dictreader = csv.DictReader(response.text.split('\r\n'))
    no_rows_csv = 0
    for item in csv_dictreader:
        no_rows_csv = no_rows_csv + 1

    assert no_rows_csv == no_rows_json, 'The number of rows are different csv vs json for ' + endpoint_router
