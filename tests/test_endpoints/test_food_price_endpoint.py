import datetime
import pytest
import logging

from decimal import Decimal
from httpx import ASGITransport, AsyncClient

from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from hdx_hapi.endpoints.models.food_price import FoodPriceResponse
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data
from tests.util.util import split_items_by_admin_level

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v2/food-security-nutrition-poverty/food-prices-market-monitor'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_food_price(event_loop, refresh_db):
    log.info('started test_get_food_price')
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one food_price in the database'


@pytest.mark.asyncio
async def test_get_food_price_params(event_loop, refresh_db):
    log.info('started test_get_food_price_params')

    for param_name, param_value in query_parameters.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={param_name: param_value}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            f'There should be at least one food_price entry for parameter "{param_name}" with value "{param_value}" '
            'in the database'
        )

    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert len(response.json()['data']) > 0, (
        'There should be at least one food_price entry for all parameters in the database'
    )


@pytest.mark.asyncio
async def test_get_food_price_result(event_loop, refresh_db):
    log.info('started test_get_food_price_result')

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
async def test_get_food_price_adm_fields(event_loop, refresh_db):
    log.info('started test_get_food_price_adm_fields')

    adm_x = FoodPriceResponse(
        resource_hdx_id='',
        market_code='',
        market_name='',
        commodity_code='',
        commodity_name='',
        commodity_category=CommodityCategory.CEREALS_TUBERS,
        currency_code='',
        unit='',
        price_flag=PriceFlag.AGGREGATE,
        price_type=PriceType.FARM_GATE,
        price=Decimal(1.5),
        lat=0.0,
        lon=0.0,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
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

    adm_x = FoodPriceResponse(
        resource_hdx_id='',
        market_code='',
        market_name='',
        commodity_code='',
        commodity_name='',
        commodity_category=CommodityCategory.CEREALS_TUBERS,
        currency_code='',
        unit='',
        price_flag=PriceFlag.AGGREGATE,
        price_type=PriceType.FARM_GATE,
        price=Decimal(1.5),
        lat=0.0,
        lon=0.0,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
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

    adm_x = FoodPriceResponse(
        resource_hdx_id='',
        market_code='',
        market_name='',
        commodity_code='',
        commodity_name='',
        commodity_category=CommodityCategory.CEREALS_TUBERS,
        currency_code='',
        unit='',
        price_flag=PriceFlag.AGGREGATE,
        price_type=PriceType.FARM_GATE,
        price=Decimal(1.5),
        lat=0.0,
        lon=0.0,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
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
async def test_get_food_price_admin_level(event_loop, refresh_db):
    log.info('started test_get_food_price_admin_level')

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

    for admin_level, count in counts_map.items():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url='http://test', params={'admin_level': admin_level}
        ) as ac:
            response = await ac.get(ENDPOINT_ROUTER)
            assert len(response.json()['data']) == count, f'Admin level {admin_level} should return {count} entries'
