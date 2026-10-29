import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from math import pow
from functools import lru_cache

from helpers import file_helper, padding_helper

@lru_cache
def to_value(input):
    parts = input[5:].split()
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

@lru_cache
def is_min_value(line, value):  
    parts = line[5:].split()
    max = int(parts[1])

    for i in range(1,max):
        prior_value = to_value("ISO2-" + parts[0] + " " + str(i))
        #logger.debug(f"Checking if line: {line} value: {value} is minimal against i: {i} prior_value: {prior_value}")
        if value == prior_value:
            return False
    return True


def solve_part3(filename):
    text = file_helper.get_text(filename)
    lines = text.splitlines()
    total = 0
    for line in lines:
        value = to_value(line)
        #logger.debug(f"Processing line: {line} value: {value}")
        if is_min_value(line, value):
            total += value  
    return total