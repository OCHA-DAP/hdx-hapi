from fastapi import Request, BackgroundTasks

from hdx_hapi.config.config import get_config
from hdx_hapi.endpoints.middleware.util.util import track_api_call, track_page_view

import logging


logger = logging.getLogger(__name__)

CONFIG = get_config()


async def mixpanel_tracking_middleware(request: Request, call_next):
    """
    Middleware to track Mixpanel events
    """

    background_tasks = BackgroundTasks()

    response = await call_next(request)

    
    if CONFIG.MIXPANEL:
        if request.url.path.startswith('/api'):
            background_tasks.add_task(track_api_call, request, response)
        elif request.url.path.startswith('/docs'):
            background_tasks.add_task(track_page_view, request, response)
    else:
        logger.warning('HDX_MIXPANEL_TOKEN environment variable is not set.')
    response.background = background_tasks

    return response
