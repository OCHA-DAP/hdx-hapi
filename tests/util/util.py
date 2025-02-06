from typing import Dict, List


def split_items_by_admin_level(response_items: List[Dict[str, str]]) -> Dict[str, int]:
    admin_0_count = len([item for item in response_items if item['admin_level'] == 0])
    admin_1_count = len([item for item in response_items if item['admin_level'] == 1])
    admin_2_count = len([item for item in response_items if item['admin_level'] == 2])
    counts_map = {
        '0': admin_0_count,
        '1': admin_1_count,
        '2': admin_2_count,
    }

    return counts_map
