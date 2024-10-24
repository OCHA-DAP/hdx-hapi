import logging
import os


from dataclasses import dataclass
from typing import Optional
from mixpanel import Mixpanel

from hdx_hapi.config.helper import create_pg_uri_from_env_without_protocol

logger = logging.getLogger(__name__)


@dataclass
class Config:
    # HAPI Database configuration
    SQL_ALCHEMY_ASYNCPG_DB_URI: str
    SQL_ALCHEMY_PSYCOPG2_DB_URI: str
    SQL_ALCHEMY_POOL_SIZE: int
    SQL_ALCHEMY_POOL_MAX_OVERFLOW: int

    HDX_DOMAIN: str
    HDX_DATASET_URL: str
    HDX_DATASET_API_URL: str
    HDX_ORGANIZATION_URL: str
    HDX_ORGANIZATION_API_URL: str

    HDX_RESOURCE_URL: str
    HDX_RESOURCE_API_URL: str

    HAPI_READTHEDOCS_OVERVIEW_URL: str

    HAPI_SERVER_URL: Optional[str]

    HAPI_IDENTIFIER_FILTERING: bool

    HAPI_USE_VAT: bool

    MIXPANEL: Optional[Mixpanel]


CONFIG = None


def get_config() -> Config:
    global CONFIG
    if not CONFIG:
        db_uri_without_protocol = create_pg_uri_from_env_without_protocol()

        sql_alchemy_asyncypg_db_uri = f'postgresql+asyncpg://{db_uri_without_protocol}'
        sql_alchemy_psycopg2_db_uri = f'postgresql+psycopg2://{db_uri_without_protocol}'
        mixpanel_token = os.getenv('HDX_MIXPANEL_TOKEN', '')
        CONFIG = Config(
            SQL_ALCHEMY_ASYNCPG_DB_URI=sql_alchemy_asyncypg_db_uri,
            SQL_ALCHEMY_PSYCOPG2_DB_URI=sql_alchemy_psycopg2_db_uri,
            SQL_ALCHEMY_POOL_SIZE=int(os.getenv('SQL_ALCHEMY_POOL_SIZE', 5)),
            SQL_ALCHEMY_POOL_MAX_OVERFLOW=int(os.getenv('SQL_ALCHEMY_POOL_MAX_OVERFLOW', 0)),
            HDX_DOMAIN=os.getenv('HDX_DOMAIN', 'https://data.humdata.org'),
            HDX_DATASET_URL=os.getenv('HDX_DATASET_URL', '{domain}/dataset/{dataset_id}'),
            HDX_RESOURCE_URL=os.getenv('HDX_DATASET_URL', '{domain}/dataset/{dataset_id}/resource/{resource_id}'),
            HDX_DATASET_API_URL=os.getenv('HDX_DATASET_API_URL', '{domain}/api/action/package_show?id={dataset_id}'),
            HDX_RESOURCE_API_URL=os.getenv(
                'HDX_RESOURCE_API_URL', '{domain}/api/action/resource_show?id={resource_id}'
            ),
            HDX_ORGANIZATION_URL=os.getenv('HDX_ORGANIZATION_URL', '{domain}/organization/{org_id}'),
            HDX_ORGANIZATION_API_URL=os.getenv(
                'HDX_ORGANIZATION_API_URL', '{domain}/api/action/organization_show?id={org_id}'
            ),
            HAPI_READTHEDOCS_OVERVIEW_URL=os.getenv(
                'HAPI_READTHEDOCS_OVERVIEW_URL', 'https://hdx-hapi.readthedocs.io/en/latest/'
            ),
            HAPI_SERVER_URL=os.getenv('HAPI_SERVER_URL', None),
            HAPI_IDENTIFIER_FILTERING=os.getenv('HAPI_IDENTIFIER_FILTERING', 'True').lower() == 'true',
            HAPI_USE_VAT=os.getenv('HAPI_USE_VAT', 'False').lower() == 'true',
            MIXPANEL=Mixpanel(mixpanel_token) if mixpanel_token else None,
        )

    return CONFIG
