from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

from collections import Counter

def time_to_limit(growth: int, limit: int) -> int:
    if limit <= 1:
        return 1

    # At t=1 the plant consists of a single element.
    time = 1
    size = 1
    branches = Counter({1: 1})  # branch_length -> count

    while size < limit:
        time += 1
        new_branches = Counter()

        for length, count in branches.items():
            length += 1          # branch grows by 1
            size += count        # newly grown elements

            if length == growth:
                half = (growth - 1) // 2

                # Branch splits into:
                #   left branch of length half
                #   right branch of length half
                #   new branch of length 1
                new_branches[half] += 2 * count
                new_branches[1] += count

                # The new branch contributes one new element.
                size += count
            else:
                new_branches[length] += count

        branches = new_branches

    return time


import common

def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    input_map = common.text_to_input_map(text)

    results_map = {}
    for id, (growth, limit) in input_map.items():
        result = time_to_limit(growth, limit)
        logger.debug(f"Processed line with ID: {id}, growth: {growth}, limit: {limit} result={result}")
        results_map[id] = result
    return sum(results_map.values())