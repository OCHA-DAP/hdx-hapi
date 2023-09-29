from datetime import date
import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_populations(event_loop, refresh_db):
    log.info('started test_get_populations')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/population')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one population entry in the database'


@pytest.mark.asyncio
async def test_get_population_params(event_loop, refresh_db):
    log.info('started test_get_population_params')

    params = {
        'gender_code': 'x',
        'age_range_code': '10-14',
        'population': 1000000,
        'dataset_provider_code': 'provider01',
        'resource_update_date_min': date(2023, 6, 1),
        'resource_update_date_max': date(2023, 6, 2),
        'location_code': 'FOO',
        'location_name': 'Foolandia',
        'admin1_code': 'FOO-XXX',
        'admin1_is_unspecified': True,
        'admin2_code': 'FOO-XXX-XXX',
        'admin2_name': 'Unspecified',
        'admin2_is_unspecified': True,
    }

    for param_name, param_value in params.items():
        async with AsyncClient(app=app, base_url="http://test", params={param_name: param_value}) as ac:
            response = await ac.get('/api/population')

        assert response.status_code == 200
        assert len(response.json()) > 0, f'There should be at least one population entry for parameter "{param_name}" with value "{param_value}" in the database'

    async with AsyncClient(app=app, base_url="http://test", params=params) as ac:
        response = await ac.get('/api/population')

    assert response.status_code == 200
    assert len(response.json()) > 0, f'There should be at least one population entry for all parameters in the database'
