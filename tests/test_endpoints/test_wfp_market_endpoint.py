import pytest
import logging

from httpx import ASGITransport, AsyncClient
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data
from hdx_hapi.endpoints.models.wfp_market import WfpMarketResponse


log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v2/metadata/wfp-market'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_wfp_market(event_loop, refresh_db):
    log.info('started test_get_wfp_market')
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one wfp_market in the database'


@pytest.mark.asyncio
async def test_get_wfp_market_params(event_loop, refresh_db):
    log.info('started test_get_wfp_market_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={param_name: param_value}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            f'There should be at least one wfp_market entry for parameter "{param_name}" with value "{param_value}" '
            'in the database'
        )

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()['data']) > 0, (
        'There should be at least one wfp_market entry for all parameters in the database'
    )


@pytest.mark.asyncio
async def test_get_wfp_market_result(event_loop, refresh_db):
    log.info('started test_get_wfp_market_result')

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()['data'][0], f'Field "{field}" not found in the response'

    for field in response.json()['data'][0]:
        assert field in expected_fields, f'Field "{field}" unexpected'

    assert len(response.json()['data'][0]) == len(expected_fields), (
        'Response has a different number of fields than expected'
    )


@pytest.mark.asyncio
async def test_get_wpf_markets_adm_fields(event_loop, refresh_db):
    log.info('started test_get_wpf_markets_adm_fields')
    adm_x = WfpMarketResponse(
        code='',
        name='',
        lat=1.1,
        lon=1.1,
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_code='FOO-XXX',
        admin1_name='Unspecified',
        admin2_code='FOO-XXX-XXX',
        admin2_name='Unspecified',
        provider_admin1_name='Province 0 Provider adm1 name',
        provider_admin2_name='District A Provider adm2 name',
        admin_level=0,
    )
    assert adm_x.admin1_code is None
    assert adm_x.admin1_name is None
    assert adm_x.admin2_code is None
    assert adm_x.admin2_name is None
    assert adm_x.admin_level == 0

    adm_x = WfpMarketResponse(
        code='',
        name='',
        lat=1.1,
        lon=1.1,
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_code='FOO-XXX',
        admin1_name='Unspecified',
        admin2_code='FOO-XXX-XXX',
        admin2_name='Unspecified',
        provider_admin1_name='Province 0 Provider adm1 name',
        provider_admin2_name='District A Provider adm2 name',
        admin_level=1,
    )

    assert adm_x.admin1_code == 'FOO-XXX'
    assert adm_x.admin1_name == 'Province 0 Provider adm1 name'
    assert adm_x.admin2_code is None
    assert adm_x.admin2_name is None
    assert adm_x.admin_level == 1

    adm_x = WfpMarketResponse(
        code='',
        name='',
        lat=1.1,
        lon=1.1,
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_code='FOO-XXX',
        admin1_name='Unspecified',
        admin2_code='FOO-XXX-XXX',
        admin2_name='Unspecified',
        provider_admin1_name='Province 0 Provider adm1 name',
        provider_admin2_name='District A Provider adm2 name',
        admin_level=2,
    )

    assert adm_x.admin1_code == 'FOO-XXX'
    assert adm_x.admin1_name == 'Province 0 Provider adm1 name'
    assert adm_x.admin2_code == 'FOO-XXX-XXX'
    assert adm_x.admin2_name == 'District A Provider adm2 name'
    assert adm_x.admin_level == 2


@pytest.mark.asyncio
async def test_get_wpf_markets_admin_level(event_loop, refresh_db):
    log.info('started test_get_wpf_markets_admin_level')

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert len(response.json()['data'][0]) == len(expected_fields), (
        'Response has a different number of fields than expected'
    )

    response_items = response.json()['data']
    admin_0_count = len(
        [item for item in response_items if item['admin1_name'] is None and item['admin2_name'] is None]
    )
    admin_1_count = len(
        [item for item in response_items if item['admin1_name'] is not None and item['admin2_name'] is None]
    )
    admin_2_count = len(
        [item for item in response_items if item['admin1_name'] is not None and item['admin2_name'] is not None]
    )
    counts_map = {
        '0': admin_0_count,
        '1': admin_1_count,
        '2': admin_2_count,
    }

    for item in response_items:
        log.info(f'{item["admin1_name"]}, {item["admin2_name"]}')
    log.info(counts_map)
    for admin_level, count in counts_map.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={'admin_level': admin_level}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)
            assert len(response.json()['data']) == count, f'Admin level {admin_level} should return {count} entries'
