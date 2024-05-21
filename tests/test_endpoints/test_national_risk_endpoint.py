import pytest
import logging

from httpx import AsyncClient
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v1/coordination-context/national-risk'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_national_risks(event_loop, refresh_db):
    log.info('started test_get_national_risks')
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one national risk entry in the database'


@pytest.mark.asyncio
async def test_get_national_risk_params(event_loop, refresh_db):
    log.info('started test_get_national_risk_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(app=app, base_url='http://test', params={param_name: param_value}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            'There should be at least one national risk entry for parameter '
            f'"{param_name}" with value "{param_value}" in the database'
        )

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert (
        len(response.json()['data']) > 0
    ), 'There should be at least one national risk entry for all parameters in the db'


@pytest.mark.asyncio
async def test_get_national_risk_result(event_loop, refresh_db):
    log.info('started test_get_national_risk_result')

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()['data'][0], f'Field "{field}" not found in the response'

    assert len(response.json()['data'][0]) == len(
        expected_fields
    ), 'Response has a different number of fields than expected'
