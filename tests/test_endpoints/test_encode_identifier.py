import base64
import pytest
import logging
from unittest.mock import ANY

from httpx import AsyncClient
from main import app
from tests.test_endpoints.endpoint_data import endpoint_data

log = logging.getLogger(__name__)

ENDPOINT_ROUTER = '/api/encode_identifier'
endpoint_data = endpoint_data[ENDPOINT_ROUTER]
query_parameters = endpoint_data['query_parameters']
expected_fields = endpoint_data['expected_fields']


@pytest.mark.asyncio
async def test_encoded_identifier_refuses_empty_parameters(event_loop, refresh_db):
    log.info('started test_encoded_identifier_refuses_empty_parameters')

    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.status_code == 422
    # The url key depends on the Pydantic version which we do not pin
    assert response.json() == {
        'detail': [
            {'type': 'missing', 'loc': ['query', 'application'], 'msg': 'Field required', 'input': None, 'url': ANY},
            {'type': 'missing', 'loc': ['query', 'email'], 'msg': 'Field required', 'input': None, 'url': ANY},
        ]
    }


@pytest.mark.asyncio
async def test_get_encoded_identifier_results(event_loop, refresh_db):
    log.info('started test_get_encoded_identifier_result')

    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    for field in expected_fields:
        assert field in response.json(), f'Field "{field}" not found in the response'

    assert len(response.json()) == len(expected_fields), 'Response has a different number of fields than expected'
    assert response.json() == {'encoded_identifier': 'd2ViX2FwcGxpY2F0aW9uXzE6aW5mb0BleGFtcGxlLmNvbQ=='}
    assert (
        base64.b64decode(response.json()['encoded_identifier']).decode('utf-8') == 'web_application_1:info@example.com'
    )


@pytest.mark.asyncio
async def test_email_validation(event_loop, refresh_db):
    log.info('started test_get_encoded_identifier_result')

    query_parameters = {'application': 'web_application', 'email': 'not_an_email'}
    async with AsyncClient(app=app, base_url='http://test', params=query_parameters) as ac:
        response = await ac.get(ENDPOINT_ROUTER)

    assert response.json() == {
        'detail': [
            {
                'type': 'value_error',
                'loc': ['query', 'email'],
                'msg': (
                    'value is not a valid email address: The email address is not valid. '
                    'It must have exactly one @-sign.'
                ),
                'input': 'not_an_email',
                'ctx': {'reason': 'The email address is not valid. It must have exactly one @-sign.'},
            }
        ]
    }
