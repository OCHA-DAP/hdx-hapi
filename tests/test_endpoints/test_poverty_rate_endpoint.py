import pytest
import logging
import datetime

from httpx import ASGITransport, AsyncClient
from hdx_hapi.endpoints.models.poverty_rate import PovertyRateResponse
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data
from tests.util.util import split_items_by_admin_level

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v2/food-security-nutrition-poverty/poverty-rate'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_poverty_rate(event_loop, refresh_db):
    log.info('started test_get_povert_rate')
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one povery rate entry in the database'


@pytest.mark.asyncio
async def test_get_poverty_rate_params(event_loop, refresh_db):
    log.info('started test_get_poverty_rate_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={param_name: param_value}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            f'There should be at least one poverty rate entry for parameter "{param_name}" with value "{param_value}" '
            'in the database'
        )

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()['data']) > 0, (
        'There should be at least one poverty rate entry for all parameters in the database'
    )


@pytest.mark.asyncio
async def test_get_poverty_rate_result(event_loop, refresh_db):
    log.info('started test_get_poverty_rate_result')

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()['data'][0], f'Field "{field}" not found in the response'

    assert len(response.json()['data'][0]) == len(expected_fields), (
        'Response has a different number of fields than expected'
    )


@pytest.mark.asyncio
async def test_get_poverty_rate_admin_level(event_loop, refresh_db):
    log.info('started test_get_poverty_rate_admin_level')

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert len(response.json()['data'][0]) == len(expected_fields), (
        'Response has a different number of fields than expected'
    )

    response_items = response.json()['data']
    counts_map = split_items_by_admin_level(response_items)

    for item in response_items:
        log.info(f'{item["admin1_name"]}')
    log.info(counts_map)
    for admin_level, count in counts_map.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={'admin_level': admin_level}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)
            assert len(response.json()['data']) == count, f'Admin level {admin_level} should return {count} entries'


@pytest.mark.asyncio
async def test_get_poverty_rate_adm_fields(event_loop, refresh_db):
    log.info('started test_get_poverty_rate_adm_fields')
    adm_x = PovertyRateResponse(
        resource_hdx_id='foo',
        mpi=0.2212,
        headcount_ratio=46.987,
        intensity_of_deprivation=49.123,
        vulnerable_to_poverty=27.123,
        in_severe_poverty=20.321,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_code='FOO-XXX',
        admin1_name='Unspecified',
        provider_admin1_name='Province 0 Provider adm1 name',
        admin_level=0,
    )
    assert adm_x.admin1_code is None
    assert adm_x.admin1_name is None
    assert adm_x.admin_level == 0

    adm_x = PovertyRateResponse(
        resource_hdx_id='foo',
        mpi=0.2212,
        headcount_ratio=46.987,
        intensity_of_deprivation=49.123,
        vulnerable_to_poverty=27.123,
        in_severe_poverty=20.321,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_code='FOO-XXX',
        admin1_name='Unspecified',
        provider_admin1_name='Province 0 Provider adm1 name',
        admin_level=1,
    )

    assert adm_x.admin1_code == 'FOO-XXX'
    assert adm_x.admin1_name == 'Province 0 Provider adm1 name'
    assert adm_x.admin_level == 1
