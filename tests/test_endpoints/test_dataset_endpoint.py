import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_datasets(event_loop, refresh_db):
    log.info('started test_get_datasets')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/dataset')
    # response = client.get('/api/dataset')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one dataset in the database'


@pytest.mark.asyncio
async def test_get_dataset_params(event_loop, refresh_db):
    log.info('started test_get_dataset_params')

    params = {
        'hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
        'title': 'Dataset #1',
        'provider_code': 'provider01',
        'provider_name': 'Provider #1',
    }

    for param_name, param_value in params.items():
        async with AsyncClient(app=app, base_url="http://test", params={param_name: param_value}) as ac:
            response = await ac.get('/api/dataset')

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one dataset entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url="http://test", params=params) as ac:
        response = await ac.get('/api/dataset')

    assert response.status_code == 200
    assert len(response.json()) > 0, f'There should be at least one dataset entry for all parameters in the database'
