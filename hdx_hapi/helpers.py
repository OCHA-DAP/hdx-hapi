import logging

from dataclasses import dataclass
from config.config import Config

logger = logging.getLogger(__name__)


@dataclass
class Context:
    config: Config


def get_dataset_url(context: Context, dataset_name: str) -> str:
    """Creates the full HDX URL for a dataset

    Args:
        context (Context): 
        dataset_name (str): Dataset name

    Returns:
        str: HDX URL for the specified dataset
    """    
    domain = context.config.HDX_DOMAIN
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    return "{domain}/dataset/{dataset}".format(domain=domain, dataset=dataset_name)
