import logging
import logging.config

logging.config.fileConfig('logging.conf')

import uvicorn  # noqa
from fastapi import FastAPI, Request  # noqa
from fastapi.responses import HTMLResponse, RedirectResponse  # noqa
from fastapi.openapi.docs import get_swagger_ui_html  # noqa

# from hdx_hapi.services.sql_alchemy_session import init_db
from hdx_hapi.endpoints.middleware.app_identifier_middleware import app_identifier_middleware  # noqa
from hdx_hapi.endpoints.middleware.mixpanel_tracking_middleware import mixpanel_tracking_middleware  # noqa

from hdx_hapi.endpoints.get_encoded_identifier import router as encoded_identifier_router  # noqa

# from hdx_hapi.endpoints.favicon import router as favicon_router  # noqa
from hdx_hapi.endpoints.get_population import router as population_router  # noqa

# from hdx_hapi.endpoints.get_operational_presence import router as operational_presence_router  # noqa
from hdx_hapi.endpoints.get_admin_level import router as admin_level_router  # noqa
from hdx_hapi.endpoints.get_hdx_metadata import router as dataset_router  # noqa
from hdx_hapi.endpoints.get_humanitarian_response import router as humanitarian_response_router  # noqa
# from hdx_hapi.endpoints.get_demographic import router as demographic_router  # noqa
# from hdx_hapi.endpoints.get_food_security import router as food_security_router  # noqa
# from hdx_hapi.endpoints.get_national_risk import router as national_risk_router  # noqa
# from hdx_hapi.endpoints.get_humanitarian_needs import router as humanitarian_needs_router  # noqa
# from hdx_hapi.endpoints.get_population_profile import router as population_profile_router  # noqa


# from hdx_hapi.endpoints.delete_example import delete_dataset
from hdx_hapi.config.config import get_config  # noqa

logger = logging.getLogger(__name__)
# import os
# logger.warning("Current folder is "+ os.getcwd())

CONFIG = get_config()

app = FastAPI(
    title='HAPI',
    description='The Humanitarian API (HAPI) is a service of the <a href="https://data.humdata.org">Humanitarian Data Exchange (HDX)</a>, part of UNOCHA\'s <a href="https://centre.humdata.org">Centre for Humanitarian Data</a>.\nThis is the reference documentation of the API. You may want to <a href="https://hdx-hapi.readthedocs.io/en/latest/">get started here</a>',  # noqa
    version='0.1.0',
    docs_url=None,
    servers=[{'url': CONFIG.HAPI_SERVER_URL}] if CONFIG.HAPI_SERVER_URL else [],
)

app.include_router(encoded_identifier_router)
# app.include_router(favicon_router)
# app.include_router(operational_presence_router)
app.include_router(population_router)
# app.include_router(food_security_router)
# app.include_router(national_risk_router)
# app.include_router(humanitarian_needs_router)
app.include_router(admin_level_router)
app.include_router(humanitarian_response_router)
# app.include_router(demographic_router)
# app.include_router(population_profile_router)
app.include_router(dataset_router)


# add middleware
@app.middleware('http')
async def app_identifier_middleware_init(request: Request, call_next):
    response = await app_identifier_middleware(request, call_next)
    return response


# add middleware
@app.middleware('http')
async def mixpanel_tracking_middleware_init(request: Request, call_next):
    response = await mixpanel_tracking_middleware(request, call_next)
    return response


@app.on_event('startup')
async def startup():
    # await init_db()
    # await populate_db()
    pass


# Adding custom favicon based on article
@app.get('/docs', include_in_schema=False)
async def swagger_ui_html(req: Request) -> HTMLResponse:
    root_path = req.scope.get('root_path', '').rstrip('/')
    openapi_url = root_path + app.openapi_url
    oauth2_redirect_url = app.swagger_ui_oauth2_redirect_url
    if oauth2_redirect_url:
        oauth2_redirect_url = root_path + oauth2_redirect_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title=app.title + ' - OpenAPI Docs',
        oauth2_redirect_url=oauth2_redirect_url,
        init_oauth=app.swagger_ui_init_oauth,
        swagger_favicon_url='/favicon.ico',
        swagger_ui_parameters=app.swagger_ui_parameters,
    )


@app.get('/', include_in_schema=False)
def home():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8844, log_config='logging.conf')
