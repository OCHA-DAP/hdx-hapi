import logging

import pytest
from httpx import ASGITransport, AsyncClient
from main import app
from unittest.mock import patch

TEST_BASE_URL = 'http://test'
TEST_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
)

log = logging.getLogger(__name__)

ENDPOINT = '/api/v2/coordination-context/operational-presence'
VERIFY_REQUEST_ENDPOINT = '/api/v2/util/verify-request'
ALLOWED_API_ENDPOINT = '/api/v2/util/version'


@pytest.mark.asyncio
async def test_direct_api_call_not_tracked():
    with patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch:
        async with AsyncClient(transport=ASGITransport(app=app), base_url=TEST_BASE_URL) as ac:
            headers = {
                'User-Agent': TEST_USER_AGENT,
                'x-forwarded-for': '127.0.0.1',
            }
            params = {'admin_level': '1', 'output_format': 'json'}
            response = await ac.get(ENDPOINT, params=params, headers=headers)

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 0, 'Direct (non-nginx-verified) API calls should not be tracked'


@pytest.mark.asyncio
async def test_nginx_verified_api_call_tracked(enable_hapi_identifier_filtering):
    with (
        patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch,
        patch(
            'hdx_hapi.endpoints.middleware.util.util.HashCodeGenerator.compute_hash',
            return_value='123456',
        ),
    ):
        async with AsyncClient(transport=ASGITransport(app=app), base_url=TEST_BASE_URL) as ac:
            headers = {
                'User-Agent': TEST_USER_AGENT,
                'x-forwarded-for': '127.0.0.1',
                'X-Original-URI': ALLOWED_API_ENDPOINT,
            }
            response = await ac.get(VERIFY_REQUEST_ENDPOINT, headers=headers)

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 1, 'Nginx-verified API calls should be tracked'

        event_name, distinct_id, event_data = send_mixpanel_event_patch.call_args.args
        assert event_name == 'hapi api call'
        assert distinct_id == '123456'
        assert event_data['identifier verification'] is True
        assert event_data['endpoint path'] == ALLOWED_API_ENDPOINT
        assert event_data['response code'] == 200


@pytest.mark.asyncio
async def test_direct_docs_page_not_tracked():
    with patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch:
        async with AsyncClient(transport=ASGITransport(app=app), base_url=TEST_BASE_URL) as ac:
            response = await ac.get('/docs')

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 0, 'Direct (non-nginx-verified) docs view should not be tracked'


@pytest.mark.asyncio
async def test_nginx_verified_docs_page_tracked(enable_hapi_identifier_filtering):
    with patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch:
        async with AsyncClient(transport=ASGITransport(app=app), base_url=TEST_BASE_URL) as ac:
            headers = {'X-Original-URI': '/docs'}
            response = await ac.get(VERIFY_REQUEST_ENDPOINT, headers=headers)

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 1, 'Nginx-verified docs page view should be tracked'

        event_name, _, event_data = send_mixpanel_event_patch.call_args.args
        assert event_name == 'hapi openapi docs view'
        assert event_data['identifier verification'] is True
