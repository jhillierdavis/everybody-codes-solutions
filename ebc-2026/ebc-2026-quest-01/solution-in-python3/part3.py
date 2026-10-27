import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper, csv_helper


def get_difference(v):
    for i in range(3, 100000):
        if i % 2 == 0:
            continue # Skip if even

        squares = (i*i)-1
        
        if squares >= v:
            logger.debug(f"v={v} i={i} squares={squares}")

            diff = squares - v
            return diff
                    
    return None

from functools import lru_cache


@lru_cache
def get_perfect_odd_square_minus_one_difference(n):
    """Calculate the difference between the nearest (greater or equal) odd perfect square minus one and n"""    
    if n <= 8: # Handle small values where the nearest odd perfect square minus one is 8
        return 8 - n

    import math

    ri = int(round(math.sqrt(n),0)) # Root approximation (to nearest integer)

    if ri % 2 == 0:
        ri +=1

    diff = (ri * ri) - 1 - n
    if diff < 0:
        ri += 2
        diff = ((ri * ri) - 1) - n
    logger.debug(f"n={n} diff={diff} ri={ri}")
    return diff
    

def solve_part3(filename):

    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:
        ans += get_perfect_odd_square_minus_one_difference(v)
    
    return ans