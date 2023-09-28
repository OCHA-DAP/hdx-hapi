import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_locations(event_loop, refresh_db):
    log.info('started test_get_locations')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/location')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one location in the database'


@pytest.mark.asyncio
async def test_get_location_params(event_loop, refresh_db):
    log.info('started test_get_location_params')

    params = {
        'code': 'FOO',
        'name': 'Foolandia'
    }

    for param_name, param_value in params.items():
        async with AsyncClient(app=app, base_url="http://test", params={param_name: param_value}) as ac:
            response = await ac.get('/api/location')

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one location entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url="http://test", params=params) as ac:
        response = await ac.get('/api/location')

    assert response.status_code == 200
    assert len(response.json()) > 0, f'There should be at least one location entry for all parameters in the database'
