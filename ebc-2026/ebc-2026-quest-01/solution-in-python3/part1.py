import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from helpers import file_helper, csv_helper


def solve_part1(filename):
    data = file_helper.get_text(filename)
    
    values = csv_helper.to_int_list(data)

    ans = 0
    for v in values:        
        
        for i in range(100):
            square = i * i
            
            if square >= v:
                logger.debug(f"v={v} square={square}")

                ans += square - v
                break

    return ans