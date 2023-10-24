import os

from fastapi import APIRouter
from fastapi.responses import FileResponse


FAVICON_PATH = 'docs/img/favicon.ico'

router = APIRouter()

favicon_path = 'favicon.ico'

@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(os.getcwd() + '/' + FAVICON_PATH)