from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

from collections import defaultdict
import heapq


def time_to_limit(growth: int, limit: int) -> int:
    """
    Return the first second at whose end the number of leaves
    reaches or exceeds limit.

    Optimized for very large growth values by processing only
    split events rather than simulating every second.
    """

    if limit <= 1:
        return 1

    half = (growth - 1) // 2

    # At t = 1:
    # one branch of length 1, one leaf
    leaves = 1

    # event_time -> number of branches that split then
    events = defaultdict(int)

    first_split = 1 + (growth - 1)
    events[first_split] = 1

    heap = [first_split]

    while leaves < limit:
        t = heapq.heappop(heap)

        count = events.pop(t)

        # each split adds exactly one leaf
        leaves += count

        if leaves >= limit:
            return t

        # branches created by each split:
        #  2 branches of length half
        #  1 branch of length 1
        #
        # Their next split times are:
        #
        #  t + (growth - half)
        #  t + (growth - 1)

        event1 = t + (growth - half)  # two branches
        event2 = t + (growth - 1)     # one branch

        if event1 not in events:
            heapq.heappush(heap, event1)
        events[event1] += 2 * count

        if event2 not in events:
            heapq.heappush(heap, event2)
        events[event2] += count

    return t


import common

def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    input_map = common.text_to_input_map(text)

    results_map = {}
    for id, (growth, limit) in input_map.items():
        result = time_to_limit(growth, limit)
        logger.debug(f"Processed line with ID: {id}, growth: {growth}, limit: {limit} result={result}")
        results_map[id] = result
    return sum(results_map.values())