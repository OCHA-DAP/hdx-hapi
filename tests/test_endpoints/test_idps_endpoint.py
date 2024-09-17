import datetime
import pytest
import logging

from httpx import AsyncClient
from hdx_hapi.endpoints.models.idps import IdpsResponse
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data

from hapi_schema.utils.enums import DTMAssessmentType

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/v1/affected-people/idps'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_get_idps(event_loop, refresh_db):
    log.info('started test_get_idps')
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert len(response.json()['data']) > 0, 'There should be at least one food security entry in the database'


@pytest.mark.asyncio
async def test_get_idps_params(event_loop, refresh_db):
    log.info('started test_get_idps_params')

    for param_name, param_value in query_parameters.items():
        print(f'{param_name}:{param_value}', flush=True)
        async with AsyncClient(app=app, base_url='http://test', params={param_name: param_value}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()['data']) > 0, (
            'There should be at least one idps entry for parameter '
            f'"{param_name}" with value "{param_value}" in the database'
        )

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 200
    assert (
        len(response.json()['data']) > 0
    ), 'There should be at least one idps entry for all parameters in the database'


@pytest.mark.asyncio
async def test_get_idps_result(event_loop, refresh_db):
    log.info('started test_get_idps_result')

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json()['data'][0], f'Field "{field}" not found in the response'

    assert len(response.json()['data'][0]) == len(
        expected_fields
    ), 'Response has a different number of fields than expected'


@pytest.mark.asyncio
async def test_get_idps_adm_fields(event_loop, refresh_db):
    log.info('started test_get_idps_adm_fields')

    idps_view_adm_specified = IdpsResponse(
        resource_hdx_id='17acb541-9431-409a-80a8-50eda7e8ebab',
        admin2_ref=1,
        reporting_round=1,
        assessment_type=DTMAssessmentType.BASELINE,
        population=500000,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_ref=1,
        admin1_code='FOO-XXX',
        admin1_name='Province 01',
        admin2_code='FOO-XXX-XXX',
        admin2_name='District A',
        location_ref=2,
        admin1_is_unspecified=False,
        admin2_is_unspecified=False,
    )

    assert True

    assert (
        idps_view_adm_specified.admin1_code == 'FOO-XXX'
    ), 'admin1_code should keep its value when admin1_is_unspecified is False'
    assert (
        idps_view_adm_specified.admin1_name == 'Province 01'
    ), 'admin1_name should keep its value when admin1_is_unspecified is False'
    assert (
        idps_view_adm_specified.admin2_code == 'FOO-XXX-XXX'
    ), 'admin2_code should keep its value when admin1_is_unspecified is False'
    assert (
        idps_view_adm_specified.admin2_name == 'District A'
    ), 'admin2_name should keep its value when admin1_is_unspecified is False'

    idps_view_adm_unspecified = IdpsResponse(
        resource_hdx_id='17acb541-9431-409a-80a8-50eda7e8ebab',
        admin2_ref=1,
        reporting_round=1,
        assessment_type=DTMAssessmentType.BASELINE,
        population=500000,
        reference_period_start=datetime.datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        reference_period_end=datetime.datetime.strptime('2023-03-31 23:59:59', '%Y-%m-%d %H:%M:%S'),
        location_code='Foolandia',
        location_name='FOO-XXX',
        admin1_ref=1,
        admin1_code='FOO-XXX',
        admin1_name='unspecified',
        admin2_code='FOO-XXX-XXX',
        admin2_name='unspecified',
        location_ref=2,
        admin1_is_unspecified=True,
        admin2_is_unspecified=True,
    )

    assert (
        idps_view_adm_unspecified.admin1_code is None
    ), 'admin1_code should be changed to None when admin1_is_unspecified is True'
    assert (
        idps_view_adm_unspecified.admin1_name is None
    ), 'admin1_name should be changed to None when admin1_is_unspecified is True'
    assert (
        idps_view_adm_unspecified.admin2_code is None
    ), 'admin2_code should be changed to None when admin1_is_unspecified is True'
    assert (
        idps_view_adm_unspecified.admin2_name is None
    ), 'admin2_name should be changed to None when admin1_is_unspecified is True'


@pytest.mark.asyncio
async def test_get_idps_admin_level(event_loop, refresh_db):
    log.info('started test_get_idps_admin_level')

    async with AsyncClient(
        app=app,
        base_url='http://test',
    ) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert len(response.json()['data'][0]) == len(
        expected_fields
    ), 'Response has a different number of fields than expected'

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

    for admin_level, count in counts_map.items():
        async with AsyncClient(app=app, base_url='http://test', params={'admin_level': admin_level}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)
            assert len(response.json()['data']) == count, f'Admin level {admin_level} should return {count} entries'
