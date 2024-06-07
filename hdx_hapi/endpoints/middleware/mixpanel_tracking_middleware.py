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
            if getattr(request.state, 'is_nginx_verify_request', False):
                original_uri_from_nginx = request.headers.get('X-Original-URI')
                if not original_uri_from_nginx:
                    logger.warning('The "hapi api call" event cannot be tracked due to missing X-Original-URI.')
                else:
                    if original_uri_from_nginx.startswith('/api'):
                        background_tasks.add_task(track_api_call, request, response)
                    elif original_uri_from_nginx.startswith('/docs'):
                        background_tasks.add_task(track_page_view, request, response)
            else:
                background_tasks.add_task(track_api_call, request, response)
        elif request.url.path.startswith('/docs'):
            background_tasks.add_task(track_page_view, request, response)
    else:
        logger.warning('HDX_MIXPANEL_TOKEN environment variable is not set.')
    response.background = background_tasks

    return response
