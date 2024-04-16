import pytest
import logging

from httpx import AsyncClient
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/encode_identifier'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_encoded_identifier(event_loop, refresh_db):
    log.info('started test_get_encoded_identifier')
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    response_items = response.json()
    assert len(response_items) == 1, 'One entry should be returned for encoded identifier'


@pytest.mark.asyncio
async def test_get_encoded_identifier_params(event_loop, refresh_db):
    log.info('started test_get_encoded_identifier_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(app=app, base_url='http://test', params={param_name: param_value}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()) == 1, (
            'There should be at one encoded_identifier entry for parameter '
            f'"{param_name}" with value "{param_value}" in the database'
        )

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()) == 1, 'There should be at one encoded_identifier entry for all parameters'


@pytest.mark.asyncio
async def test_get_encoded_identifier_results(event_loop, refresh_db):
    log.info('started test_get_encoded_identifier_result')

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json(), f'Field "{field}" not found in the response'

    assert len(response.json()) == len(expected_fields), 'Response has a different number of fields than expected'
    assert response.json() == {'encoded_identifier': 'web_application_1:info@example.com'}
