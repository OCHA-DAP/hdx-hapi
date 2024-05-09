import logging
import time

import pytest
from httpx import AsyncClient
from main import app
from unittest.mock import patch

TEST_BASE_URL = 'http://test'
TEST_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
)

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_tracking_endpoint_success():
    with patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch, patch(
        'hdx_hapi.endpoints.middleware.util.util.HashCodeGenerator.compute_hash',
        return_value='123456',
    ):
        async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
            headers = {
                'User-Agent': TEST_USER_AGENT,
                'HTTP_X_REAL_IP': '127.0.0.1',
            }
            params = {'admin_level': '1', 'output_format': 'json'}
            response = await ac.get('/api/v1/themes/3w', params=params, headers=headers)

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 1, 'API calls should be tracked'

        expected_mixpanel_dict = {
            'endpoint name': '/api/v1/themes/3w',
            'query params': ['admin_level', 'output_format'],
            'time': pytest.approx(time.time()),
            'app name': None,
            'output format': 'json',
            'admin level': '1',
            'server side': True,
            'response code': 200,
            'user agent': TEST_USER_AGENT,
            'ip': '127.0.0.1',
            '$os': 'Windows',
            '$browser': 'Chrome',
            '$browser_version': '124',
            '$current_url': f'{TEST_BASE_URL}/api/v1/themes/3w?admin_level=1&output_format=json',
        }

        (
            send_mixpanel_event_patch.assert_called_once_with('api call', '123456', expected_mixpanel_dict),
            'Parameters do not match the expected ones',
        )


@pytest.mark.asyncio
async def test_docs_page_tracked():
    with patch('hdx_hapi.endpoints.middleware.util.util.send_mixpanel_event') as send_mixpanel_event_patch:
        async with AsyncClient(app=app, base_url=TEST_BASE_URL) as ac:
            response = await ac.get('/docs')

        assert response.status_code == 200
        assert send_mixpanel_event_patch.call_count == 1, 'Docs page should be tracked as a page view'
