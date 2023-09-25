import os
import uvicorn

from elasticapm.contrib.starlette import ElasticAPM, make_apm_client

from main import app

apm = make_apm_client({
    'SERVICE_NAME': os.getenv('ELASTIC_APM_SERVICE_NAME', 'HAPI'),
    'SERVER_URL': os.getenv('ELASTIC_APM_SERVER_URL', 'http://localhost:8200'),
    'SECRET_TOKEN': os.getenv('ELASTIC_APM_SECRET_TOKEN'),
    'ENVIRONMENT': os.getenv('ELASTIC_APM_ENVIRONMENT', 'local'),
    'ENABLED': os.getenv('ELASTIC_APM_ENABLED')
})
app.add_middleware(ElasticAPM, client=apm)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8844, log_config='logging.conf')