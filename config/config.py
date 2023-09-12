from dataclasses import dataclass

import os


@dataclass
class Config:
    HDX_DOMAIN: str

CONFIG = None

def get_config() -> Config:
    global CONFIG
    if not CONFIG:
        CONFIG = Config(
            HDX_DOMAIN=os.getenv('HDX_DOMAIN', 'https://hdx.website.url'),
        )

    return CONFIG