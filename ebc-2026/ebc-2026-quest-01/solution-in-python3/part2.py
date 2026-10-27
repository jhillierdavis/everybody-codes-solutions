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
    if n <= 8: # Handle small values where the nearest perimeter is 8
        return 8 - n

    side = (n - 1) // 4 # Approximate side length of the square with perimeter just below 
    diff = 4 * (side + 1) - n
    return diff


def solve_part2(filename):
    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:
        ans += get_perimeter_difference(v)

    return ans