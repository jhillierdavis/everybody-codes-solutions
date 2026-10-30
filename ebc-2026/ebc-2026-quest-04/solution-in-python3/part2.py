import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from collections import defaultdict
from helpers import file_helper


def solve_part2(filename):
    text = file_helper.get_text(filename)

    parts_map, times_map = get_parts_and_times_maps(text)
  
    sorted_data = sort_order_by_parts_and_time(parts_map, times_map)

    ans = calculate_checksum(sorted_data)
    return ans


def get_parts_and_times_maps(text):
    parts_map = defaultdict(set)
    times_map = defaultdict(int)
    for l in text.splitlines():
            logger.debug(f"{l}")
            parts = l.split()
            id = int(parts[0].split("=")[1])
            quest = int(parts[1].split("=")[1])
            part = int(parts[2].split("=")[1])
            time = int(parts[3].split("=")[1])
            times_map[id] += time
            parts_map[id].add((quest, part))

            logger.debug(f"parts_map: {parts_map}")
            logger.debug(f"times_map: {times_map}")
    return parts_map, times_map


def get_summary_data(parts_map, times_map):
    summary_data = []
    for id, size in parts_map.items():  
        #logger.debug(f"ID {id} has parts: {size}")
        summary_data.append({"id": int(id), "num_parts": len(size), "total_time": -times_map[id]})

    return summary_data


def sort_order_by_parts_and_time(parts_map, times_map):
    summary_data = get_summary_data(parts_map, times_map)
    # Sort by number of parts (highest first) then time (lowest first)
    sorted_data = sorted(
        summary_data,
            key=lambda x: (x["num_parts"], x["total_time"])
        )
    sorted_data.reverse()
    return sorted_data


def calculate_checksum(sorted_data):
    ans = 0
    #logger.debug(f"sorted_data: {sorted_data}")
    values = [abs(item["total_time"]) for item in sorted_data]
    #logger.debug(f"values: {values}")
    for i  in range(len(values)):
        ans += (1 + i) * values[i]
 
    return ans