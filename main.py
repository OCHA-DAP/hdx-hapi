import logging
import logging.config
logging.config.fileConfig('logging.conf')

import uvicorn
from fastapi import FastAPI

from hdx_hapi.services.sql_alchemy_session import init_db

from hdx_hapi.endpoints.get_operational_presence import router as operational_presence_router
from hdx_hapi.endpoints.get_admin_level import router as admin_level_router
from hdx_hapi.endpoints.get_hdx_metadata import router as dataset_router
from hdx_hapi.endpoints.get_humanitarian_response import router as humanitarian_response_router
from hdx_hapi.endpoints.get_demographic import router as demographic_router
from hdx_hapi.endpoints.get_population import router as population_router

# from hdx_hapi.endpoints.delete_example import delete_dataset

logger = logging.getLogger(__name__)
# import os
# logger.warning("Current folder is "+ os.getcwd())

app = FastAPI(
    title='HAPI',
    description='The Humanitarian API (HAPI) is a service of the <a href="https://data.humdata.org">Humanitarian Data Exchange (HDX)</a>, part of UNOCHA\'s <a href="https://centre.humdata.org">Centre for Humanitarian Data</a>.\nThis is the reference documentation of the API. You may want to <a href="fix/this/link">TBD - get started here</a>',
    version='0.0.1'
)

app.include_router(operational_presence_router)
app.include_router(admin_level_router)
app.include_router(dataset_router)
app.include_router(humanitarian_response_router)
app.include_router(demographic_router)
app.include_router(population_router)

@app.on_event('startup')
async def startup():
    # await init_db()
    # await populate_db()
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8844, log_config='logging.conf')
