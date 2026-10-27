import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper, csv_helper


def solve_part3(filename):
    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:
        for i in range(3, 100000):
            if i % 2 == 0:
                continue # Skip if even

            squares = (i*i)-1
            
            if squares >= v:
                logger.debug(f"v={v} i={i} squares={squares}")

                ans += squares - v
                break

    return ans