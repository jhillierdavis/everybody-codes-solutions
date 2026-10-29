import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from math import pow

def to_value(input):
    parts = input[4:].split()
    logger.debug(f"Parts extracted from input: {parts}")

    ans = 0
    size = len(parts[0])
    for i in range(size):
        p1 = int(parts[0][i])
        p2 = int(parts[1][i])
        value = p2 * pow (p1, (size-1)-i)
        logger.debug(f"i: {i} p1: {p1}, p2: {p2}, size: {size}, value: {value}")
                
        ans += int(value)
    return ans

from helpers import file_helper

def solve_part1(filename):
    text = file_helper.get_text(filename)
    lines = text.splitlines()
    total = 0
    for line in lines:
        total += to_value(line)
    return total