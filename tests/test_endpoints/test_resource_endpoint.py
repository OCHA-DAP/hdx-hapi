from datetime import date
import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_resources(event_loop, refresh_db):
    log.info('started test_get_resources')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/resource')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one resource in the database'


@pytest.mark.asyncio
async def test_get_resource_params(event_loop, refresh_db):
    log.info('started test_get_resource_params')

    params = {
        'hdx_id': '90deb235-1bf5-4bae-b231-3393222c2d01',
        'format': 'csv',
        'update_date_min': date(2023, 6, 1),
        'update_date_max': date(2023, 6, 2),
        'is_hxl': True,
        'dataset_hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
        'dataset_title': 'Dataset #1',
        'dataset_provider_code': 'provider01',
        'dataset_provider_name': 'Provider #1',
    }

    for param_name, param_value in params.items():
        async with AsyncClient(app=app, base_url="http://test", params={param_name: param_value}) as ac:
            response = await ac.get('/api/resource')

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one resource entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url="http://test", params=params) as ac:
        response = await ac.get('/api/resource')

    assert response.status_code == 200
    assert len(response.json()) > 0, f'There should be at least one resource entry for all parameters in the database'
