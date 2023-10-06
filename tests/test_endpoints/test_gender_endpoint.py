import pytest
import logging
import csv
from httpx import AsyncClient
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/gender'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']

def check_output_format(output_format, response):
    assert response.status_code == 200
    if output_format == 'json':
        assert len(response.json()) > 0, 'There should be at least one gender in the database'
    if output_format == 'csv':
        assert response.headers.get('content-type') == 'text/csv; charset=utf-8', 'The output should be in csv format'


@pytest.mark.parametrize("output_format", ['json','csv'])
@pytest.mark.asyncio
async def test_get_genders(event_loop, refresh_db, output_format):
    log.info('started test_get_genders')
    params={"output_format":output_format}
    async with AsyncClient(app=app, base_url='http://test',params=params) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    check_output_format(output_format, response)


@pytest.mark.parametrize("output_format", ['json'])
@pytest.mark.asyncio
async def test_get_gender_params(event_loop, refresh_db, output_format):
    log.info('started test_get_gender_params')
    query_parameters["output_format"]=output_format
    for param_name, param_value in query_parameters.items():
        async with AsyncClient(app=app, base_url='http://test', params={param_name: param_value}) as ac:
            response = await ac.get(ENDPOINT_ROUTER)

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one gender entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    check_output_format(output_format, response)


@pytest.mark.parametrize("output_format", ['json'])
@pytest.mark.asyncio
async def test_get_gender_result(event_loop, refresh_db, output_format):
    log.info('started test_get_gender_result')
    query_parameters["output_format"]=output_format
    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    check_output_format(output_format, response)

    for field in expected_fields:
        assert field in response.json()[0], f'Field "{field}" not found in the response'

    assert len(response.json()[0]) == len(expected_fields), f'Response has a different number of fields than expected'

@pytest.mark.asyncio
async def test_get_genders_csv(event_loop, refresh_db):
    log.info('started test_get_genders')
    async with AsyncClient(app=app, base_url='http://test', params={"output_format":"csv"}) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'text/csv; charset=utf-8', 'The output should be in csv format'
    try:

        csv_dictreader = csv.DictReader(response.text.split('\r\n'))
        i=0
        for item in csv_dictreader:
            log.debug(item)
            i=i+1
        assert True
    except Exception as ex:
        assert False, 'The output is not csv'
    