from typing import Dict, List


def split_items_by_admin_level(response_items: List[Dict[str, str]]) -> Dict[str, int]:
    admin_0_count = len(
        [
            item
            for item in response_items
            if item['admin1_name'] is None
            and item['provider_admin1_name'] == ''
            and item['admin2_name'] is None
            and item['provider_admin2_name'] == ''
        ]
    )
    admin_1_count = len(
        [
            item
            for item in response_items
            if (item['admin1_name'] is not None or item['provider_admin1_name'] != '')
            and item['admin2_name'] is None
            and item['provider_admin2_name'] == ''
        ]
    )
    admin_2_count = len(
        [
            item
            for item in response_items
            if (item['admin1_name'] is not None or item['provider_admin1_name'] != '')
            and (item['admin2_name'] is not None or item['provider_admin2_name'] != '')
        ]
    )
    counts_map = {
        '0': admin_0_count,
        '1': admin_1_count,
        '2': admin_2_count,
    }

    return counts_map
