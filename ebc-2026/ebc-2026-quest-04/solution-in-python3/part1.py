import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from collections import defaultdict
from helpers import file_helper

def solve_part1(filename):
    text = file_helper.get_text(filename)

    map_times = defaultdict(int)
    for l in text.splitlines():
            logger.debug(f"{l}")
            parts = l.split()
            id = parts[0].split("=")[1]
            time = int(parts[3].split("=")[1])
            map_times[id] += time

    logger.debug(f"{map_times}")

    ans = 0

    values = sorted(map_times.values())
    for i  in range(len(values)):
        ans += (1 + i) * values[i]
 
    return ans