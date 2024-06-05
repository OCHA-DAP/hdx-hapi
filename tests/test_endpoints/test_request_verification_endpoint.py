import pytest

from httpx import AsyncClient
from main import app


ENDPOINT_ROUTER = '/api/v1/util/verify-request'

APP_IDENTIFIER = 'cHl0ZXN0czpweXRlc3RzQGh1bWRhdGEub3Jn'
URL_WITHOUT_APP_IDENTIFIER = 'http://localhost/api/v1/population-social/population?output_format=json&limit=10&offset=0'
URL_WITH_APP_IDENTIFIER = (
    'http://localhost/api/v1/population-social/population?output_format=json&'
    f'app_identifier={APP_IDENTIFIER}&limit=10&offset=0'
)


@pytest.mark.asyncio
async def test_verify_request(event_loop, refresh_db, enable_hapi_identifier_filtering):
    status_code = await _perform_request({})
    assert status_code == 403

    headers = {'X-Original-URI': URL_WITHOUT_APP_IDENTIFIER}
    status_code = await _perform_request(headers)
    assert status_code == 403

    headers = {'X-Original-URI': URL_WITHOUT_APP_IDENTIFIER, 'X-HDX-HAPI-APP-IDENTIFIER': APP_IDENTIFIER}
    status_code = await _perform_request(headers)
    assert status_code == 200

    headers = {'X-Original-URI': URL_WITH_APP_IDENTIFIER}
    status_code = await _perform_request(headers)
    assert status_code == 200


async def _perform_request(headers) -> int:
    async with AsyncClient(app=app, base_url='http://test', headers=headers) as ac:
        response = await ac.get(ENDPOINT_ROUTER)
    return response.status_code
