from helpers import logging_helper, file_helper, parent_child_helper

logger = logging_helper.get_logger_instance()

import common


def solve_part2(filename):
    text = file_helper.get_text(filename)
    ingredients_map = common.get_ingredients_map(text)

    keys = parent_child_helper.get_all_unique_ancestors_of_child(ingredients_map, 'NULL')
    logger.debug("Keys with 'NULL' value: %s", keys)
    return len(keys)