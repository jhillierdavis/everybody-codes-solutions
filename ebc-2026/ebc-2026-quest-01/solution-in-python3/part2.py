import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper, csv_helper

from functools import lru_cache


@lru_cache
def get_perimeter_difference(n):
    if n <= 8: # Handle small values where the nearest perimeter is 8 (3x3 square with empty center)
        return 8 - n

    inner_side = (n - 1) // 4 # Approximate inner side length of the target square perimeter
    diff = 4 * (inner_side + 1) - n
    return diff


def solve_part2(filename):
    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:
        ans += get_perimeter_difference(v)

    return ans