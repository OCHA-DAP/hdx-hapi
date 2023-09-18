from dataclasses import dataclass
import logging
import os

logger = logging.getLogger(__name__)

@dataclass
class Config:
    # HAPI Database configuration
    SQL_ALCHEMY_ASYNCPG_DB_URI: str
    SQL_ALCHEMY_PSYCOPG2_DB_URI: str

    HDX_DOMAIN: str
    HDX_DATASET_URL: str
    HDX_DATASET_API_URL: str
    HDX_ORGANIZATION_URL: str


CONFIG = None


def get_config() -> Config:
    
    global CONFIG
    if not CONFIG:
        hapi_db_name = os.getenv('HAPI_DB_NAME', 'hapi')
        hapi_db_user = os.getenv('HAPI_DB_USER', 'hapi')
        hapi_db_pass = os.getenv('HAPI_DB_PASS', 'hapi')
        hapi_db_host = os.getenv('HAPI_DB_HOST', 'db')
        hapi_db_port = int(os.getenv('HAPI_DB_PORT', 5432))

        sql_alchemy_asyncypg_db_uri = \
            f'postgresql+asyncpg://{hapi_db_user}:{hapi_db_pass}@{hapi_db_host}:{hapi_db_port}/{hapi_db_name}'
        sql_alchemy_psycopg2_db_uri = \
            f'postgresql+psycopg2://{hapi_db_user}:{hapi_db_pass}@{hapi_db_host}:{hapi_db_port}/{hapi_db_name}'
        CONFIG = Config(
            SQL_ALCHEMY_ASYNCPG_DB_URI=sql_alchemy_asyncypg_db_uri,
            SQL_ALCHEMY_PSYCOPG2_DB_URI=sql_alchemy_psycopg2_db_uri,

            HDX_DOMAIN=os.getenv('HDX_DOMAIN', 'https://data.humdata.org'),
            HDX_DATASET_URL=os.getenv('HDX_DATASET_URL', '{domain}/dataset/{dataset_id}'),
            HDX_DATASET_API_URL=os.getenv('HDX_DATASET_API_URL', '{domain}/api/action/package_show?id={dataset_id}'),
            HDX_ORGANIZATION_URL=os.getenv('HDX_ORGANIZATION_URL', '{domain}/organization/{org_id}'),
        )

    return CONFIG
