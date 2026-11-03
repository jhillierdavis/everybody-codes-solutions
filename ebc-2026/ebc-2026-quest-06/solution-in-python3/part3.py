from helpers import logging_helper, file_helper, parent_child_helper

logger = logging_helper.get_logger_instance()

import common


def find_intersections_for_at_least_two_variants(ingredients_map):
    # Find all unique keys that are common ancestors of at least two of the NULL variants

    v1 = parent_child_helper.get_all_unique_ancestors_of_child(ingredients_map, 'NULLv1')
    v2 = parent_child_helper.get_all_unique_ancestors_of_child(ingredients_map, 'NULLv2')
    v3 = parent_child_helper.get_all_unique_ancestors_of_child(ingredients_map, 'NULLv3')

    s = set()
    for v in v1.intersection(v2):
        s.add(v)
    for v in v1.intersection(v3):
        s.add(v)

    for v in v2.intersection(v3):
        s.add(v)

    logger.debug("Keys containing 'NULLv1': %s", v1)
    logger.debug("Keys containing 'NULLv2': %s", v2)
    logger.debug("Keys containing 'NULLv3': %s", v3)

    return s


def solve_part3(filename):
    text = file_helper.get_text(filename)
    ingredients_map = common.get_ingredients_map(text)

    intersection_set = find_intersections_for_at_least_two_variants(ingredients_map)
    return len(intersection_set)