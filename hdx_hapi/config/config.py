from dataclasses import dataclass
import logging
import os

logger = logging.getLogger(__name__)

@dataclass
class Config:
    HDX_DOMAIN: str
    HDX_DATASET_URL: str
    HDX_DATASET_API_URL: str


CONFIG = None


def get_config() -> Config:
    
    global CONFIG

    if not CONFIG:
        CONFIG = Config(
            HDX_DOMAIN=os.getenv('HDX_DOMAIN', 'https://data.humdata.org'),
            HDX_DATASET_URL=os.getenv('HDX_DATASET_URL', '{domain}/dataset/{dataset_id}'),
            HDX_DATASET_API_URL=os.getenv('HDX_DATASET_API_URL', '{domain}/api/action/package_show?id={dataset_id}'),
        )

    return CONFIG
