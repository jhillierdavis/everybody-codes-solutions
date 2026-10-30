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

    times_map = get_times_map_from_input(text)

    ans = calculate_checksum(times_map)
    return ans


def get_times_map_from_input(text):
    times_map = defaultdict(int)
    for l in text.splitlines():
            logger.debug(f"{l}")
            parts = l.split()
            id = int(parts[0].split("=")[1])
            time = int(parts[3].split("=")[1])
            times_map[id] += time

    logger.debug(f"times_map: {times_map}")     
    return times_map


def calculate_checksum(times_map):
    sorted_times_map = sorted(times_map.values())
    logger.debug(f"sorted_times_map: {sorted_times_map}")
    ans = 0
    for i  in range(len(sorted_times_map)):
        ans += (1 + i) * sorted_times_map[i]
    return ans