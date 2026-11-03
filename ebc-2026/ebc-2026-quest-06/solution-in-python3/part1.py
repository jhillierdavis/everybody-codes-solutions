from helpers import logging_helper, file_helper, parent_child_helper

logger = logging_helper.get_logger_instance()

import common


def solve_part1(filename):
    text = file_helper.get_text(filename)

    ingredients_map = common.get_ingredients_map(text)

    null_ingredients_set = parent_child_helper.get_all_unique_descendent_references_for_parent(ingredients_map, 'NULL')
    logger.debug("NULL ingredients set: %s", null_ingredients_set)
    return len(null_ingredients_set)