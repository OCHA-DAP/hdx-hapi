import json
import os
import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/admin1'
with open(os.path.join(os.path.dirname(__file__), 'endpoint_data.json'), 'r') as file:
    endpoint_data = json.load(file)[ENDPOINT_ROUTER]
    query_parameters = endpoint_data['query_parameters']
    expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_admin1(event_loop, refresh_db):
    log.info('started test_get_admin1')
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one admin1 entry in the database'


@pytest.mark.asyncio
async def test_get_admin1_params(event_loop, refresh_db):
    log.info('started test_get_admin1_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(app=app, base_url='http://test', params={param_name: param_value}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one admin1 entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()) > 0, f'There should be at least one admin1 entry for all parameters in the database'


@pytest.mark.asyncio
async def test_get_admin1_result(event_loop, refresh_db):
    log.info('started test_get_admin1_result')

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()[0], f'Field "{field}" not found in the response'

    assert len(response.json()[0]) == len(expected_fields), f'Response has a different number of fields than expected'