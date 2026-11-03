from helpers import logging_helper, file_helper,  padding_helper

logger = logging_helper.get_logger_instance()

from math import pow
from functools import lru_cache


@lru_cache
def to_value(input):
    parts = input[4:].split()
    #logger.debug(f"Parts extracted from input: {parts}")

    ans = 0
    size = len(parts[1])
    p1v = parts[0]
    if len(parts[0]) < size:
        p1v = padding_helper.prefix_pad(parts[0], size)
    elif len(parts[0]) > size:
        p1v = p1v[len(parts[0]) - size:]

    for i in range(size):
        p1 = int(p1v[i])
        p2 = int(parts[1][i])
        power = (size-1)-i
        value = p2 * int(pow (p1, power))
        #logger.debug(f"i: {i} p1: {p1}, p2: {p2}, size: {size}, power: {power}, value: {value}")
                
        ans += value
    return ans


def solve_part2(filename):
    text = file_helper.get_text(filename)
    lines = text.splitlines()
    total = 0
    for line in lines:
        total += to_value(line)
    return total