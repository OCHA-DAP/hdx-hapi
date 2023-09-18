from dataclasses import dataclass

import os


@dataclass
class Config:
    HDX_DOMAIN: str
    HDX_ORGANIZATION_URL: str

CONFIG = None

def get_config() -> Config:
    global CONFIG
    if not CONFIG:
        CONFIG = Config(
            HDX_DOMAIN=os.getenv('HDX_DOMAIN', 'https://data.humdata.org'),
            HDX_ORGANIZATION_URL=os.getenv('HDX_ORGANIZATION_URL', '{domain}/organization/{org_id}'),
        )

    return CONFIG