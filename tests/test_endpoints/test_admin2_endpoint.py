import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_admin2(event_loop, refresh_db):
    log.info('started test_get_admin2')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/admin2')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one admin2 entry in the database'
    
