import logging
import hashlib
import time
import ua_parser.user_agent_parser as useragent
from fastapi import Request, Response

from hdx_hapi.config.config import mixpanel


logger = logging.getLogger(__name__)

async def track_api_call(request: Request, response: Response):
    current_url = str(request.url)
    endpoint = request.url.path
    query_params = list(request.query_params.keys())
    output_format = request.query_params.get('output_format', '')
    admin_level = request.query_params.get('admin_level', '')

    app_name = getattr(request.state, 'app_name', None)
    user_agent_string = request.headers.get('user-agent', '')
    ip_address = request.headers.get('HTTP_X_REAL_IP', '')

    response_code = response.status_code

    distinct_id = HashCodeGenerator({'ip': ip_address, 'ua': user_agent_string}).compute_hash()
    event_time = time.time()

    ua_dict = useragent.Parse(user_agent_string)
    ua_os = ua_dict.get('os', {}).get('family')
    ua_browser = ua_dict.get('user_agent', {}).get('family')
    ua_browser_version = ua_dict.get('user_agent', {}).get('major')

    mixpanel.track(distinct_id, 'api call', {
        'endpoint name': endpoint,
        'query params': query_params,
        'time': event_time,
        'app name': app_name,
        'output format': output_format,
        'admin level': admin_level,
        'server side': True,
        'response code': response_code,
        'user agent': user_agent_string,
        'ip': ip_address,
        '$os': ua_os,
        '$browser': ua_browser,
        '$browser_version': ua_browser_version,
        '$current_url': current_url
    })


class HashCodeGenerator(object):
    """
    Works only on simple dictionaries (not nested). At least the specified fields need to not be nested.
    """
    def __init__(self, src_dict, field_list=None):
        if not field_list and src_dict:
            field_list = list(src_dict.keys())

        field_list.sort()
        try:
            self.__inner_string = ''
            if field_list and src_dict:
                for field in field_list:
                    self.__inner_string += '{}-{},'.format(field, src_dict.get(field))
            else:
                raise Exception('Either field list or source dict are null')
        except Exception:
            raise Exception('Exception while trying to generate hash code')

    def compute_hash(self):
        hash_builder = hashlib.md5()
        hash_builder.update(self.__inner_string.encode())
        hash_code = hash_builder.hexdigest()
        logger.debug('Generated code for {} is {}'.format(self.__inner_string, hash_code))
        return hash_code
