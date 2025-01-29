import pytest
import logging

from httpx import ASGITransport, AsyncClient
from main import app
from hdx_hapi.endpoints.util.util import AdminLevel
from tests.test_endpoints.endpoint_data import endpoint_data


log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v1/metadata/data-availability'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_data_availability(event_loop, refresh_db):
    log.info('started test_get_data_availability')
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one data availability row in the database'


@pytest.mark.asyncio
async def test_get_data_availability_params(event_loop, refresh_db):
    log.info('started test_get_data_availability_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={param_name: param_value}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            f'There should be at least one data availability entry for parameter "{param_name}" '
            f'with value "{param_value}" in the database'
        )

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()['data']) > 0, (
        'There should be at least one availability row for all parameters in the database'
    )


@pytest.mark.asyncio
async def test_get_data_availability_result(event_loop, refresh_db):
    log.info('started test_get_data_availability_result')

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()['data'][0], f'Field "{field}" not found in the response'

    assert len(response.json()['data'][0]) == len(expected_fields), (
        'Response has a different number of fields than expected'
    )


@pytest.mark.asyncio
async def test_get_data_availability_for_admin_level_filter(event_loop, refresh_db):
    log.info('started test_get_data_availability_result')

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
        params={
            'admin_level': AdminLevel.ZERO.value,
        },
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
        results = response.json()['data']
        assert len(results) > 0
        for item in results:
            assert item['admin1_code'] is None
            assert item['admin2_code'] is None
            assert item['admin1_name'] is None
            assert item['admin2_name'] is None

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
        params={
            'admin_level': AdminLevel.ONE.value,
        },
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
        results = response.json()['data']
        assert len(results) > 0
        for item in results:
            assert item['admin2_code'] is None
            assert item['admin2_name'] is None
            assert item['admin1_code'] is not None
            assert item['admin1_name'] is not None

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
        params={
            'admin_level': AdminLevel.TWO.value,
        },
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
        results = response.json()['data']
        assert len(results) > 0
        for item in results:
            assert item['admin2_code'] is not None
            assert item['admin2_name'] is not None
            assert item['admin1_code'] is not None
            assert item['admin1_name'] is not None
