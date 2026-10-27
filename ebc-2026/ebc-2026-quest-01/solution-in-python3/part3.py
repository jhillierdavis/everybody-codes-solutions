import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper


def solve_part3(filename):
    data = file_helper.get_text(filename)    

    ans = 0
    values = data.split(',')
    for v in values:
        vi = int(v)
        
        for i in range(3, 100000):
            if i % 2 == 0:
                continue # Skip if even

            squares = (i*i)-1
            
            if squares >= vi:
                logger.debug(f"vi={vi} i={i} squares={squares}")

                ans += squares - vi
                break

    return ans