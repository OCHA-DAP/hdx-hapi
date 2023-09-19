import logging

from dataclasses import dataclass
from hdx_hapi.config.config import Config

logger = logging.getLogger(__name__)


@dataclass
class Context:
    config: Config


def get_dataset_url(context: Context, dataset_id: str) -> str:
    """Creates the full HDX URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX URL for the specified dataset
    """    
    domain = context.config.HDX_DOMAIN
    dataset_url = context.config.HDX_DATASET_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    return dataset_url.format(domain=domain, dataset_id=dataset_id)

def get_dataset_api_url(context: Context, dataset_id: str) -> str:
    """Creates the full HDX API URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX API URL for the specified dataset (package_show)
    """    
    domain = context.config.HDX_DOMAIN
    dataset_api_url = context.config.HDX_DATASET_API_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    return dataset_api_url.format(domain=domain, dataset_id=dataset_id)