import pytest
import logging

from httpx import AsyncClient
from main import app

log = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_get_orgs(event_loop, refresh_db):
    log.info('started test_get_orgs')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/api/org')
    assert response.status_code == 200
    assert len(response.json()) > 0, 'There should be at least one org in the database'
