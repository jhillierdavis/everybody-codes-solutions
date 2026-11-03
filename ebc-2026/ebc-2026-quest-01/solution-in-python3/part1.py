from helpers import logging_helper, file_helper, csv_helper

logger = logging_helper.get_logger_instance()

from functools import lru_cache


@lru_cache
def get_perfect_square_difference(n):
    """Calculate the difference between the nearest (greater or equal) perfect square and n"""
    import math

    root = math.sqrt(n)

    x = math.ceil(root) # Round up to the next integer if root is not an integer

    diff = x * x - n
    logger.debug(f"n={n} x={x} diff={diff}")
    return diff



def solve_part1(filename):
    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:        
        ans += get_perfect_square_difference(v)

    return ans