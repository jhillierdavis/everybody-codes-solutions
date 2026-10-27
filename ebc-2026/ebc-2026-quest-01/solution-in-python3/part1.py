import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper


def solve_part1(filename):
    data = file_helper.get_text(filename)

    ans = 0
    values = data.split(',')
    for v in values:
        vi = int(v)
        
        for i in range(100):
            square = i * i
            
            if square >= vi:
                logger.debug(f"vi={vi} square={square}")

                ans += square - vi
                break

    return ans