from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

from collections import Counter

def time_to_limit(growth: int, limit: int) -> int:
    """
    Return the first second at whose end the number of leaves
    is greater than or equal to limit.
    """

    if limit <= 1:
        return 1

    time = 1
    leaves = 1

    # branch_length -> number of branches of that length
    branches = Counter({1: 1})

    while leaves < limit:
        time += 1
        next_branches = Counter()

        for length, count in branches.items():
            length += 1

            if length == growth:
                half = (growth - 1) // 2

                # Split into:
                #   two branches of length half
                #   one new branch of length 1
                next_branches[half] += 2 * count
                next_branches[1] += count

                # Each split adds one extra leaf.
                leaves += count
            else:
                next_branches[length] += count

        branches = next_branches

    return time


import common

def solve_part2(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    input_map = common.text_to_input_map(text)

    results_map = {}
    for id, (growth, limit) in input_map.items():
        result = time_to_limit(growth, limit)
        logger.debug(f"Processed line with ID: {id}, growth: {growth}, limit: {limit} result={result}")
        results_map[id] = result
    return sum(results_map.values())