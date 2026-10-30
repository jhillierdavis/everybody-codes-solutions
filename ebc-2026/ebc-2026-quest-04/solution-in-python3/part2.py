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

    map_parts = defaultdict(set)
    map_times = defaultdict(int)
    data = []
    for l in text.splitlines():
            logger.debug(f"{l}")
            parts = l.split()
            id = parts[0].split("=")[1]
            quest = parts[1].split("=")[1]
            part = parts[2].split("=")[1]
            time = int(parts[3].split("=")[1])
            map_times[id] += time
            map_parts[id].add((quest, part))
            data.append({"id": int(id), "quest": int(quest), "part": int(part), "time": int(time)})

    logger.debug(f"map-parts: {map_parts}")
    logger.debug(f"map-times: {map_times}")
    logger.debug(f"data: {data}")

    map_ordered = {}
    for id, size in map_parts.items():
        map_ordered[id] =  map_times[id] / len(size)

    #logger.debug(f"map-ordered: {map_ordered}")
    ordered_ids = sorted(map_ordered, key=lambda x: map_ordered[x])
    #logger.debug(f"ordered-ids: {ordered_ids}")

    ans = 0
    for i, id in enumerate(ordered_ids):
        #logger.debug(f"Ordered ID {i}: {id}")
        ans += (i + 1) * map_times[id]

    summary_data = []
    for id, size in map_parts.items():  
        #logger.debug(f"ID {id} has parts: {size}")
        summary_data.append({"id": int(id), "num_parts": len(size), "total_time": -map_times[id]})

    # Sort by number of parts (highest first) then time (lowest first)
    sorted_data = sorted(
        summary_data,
            key=lambda x: (x["num_parts"], x["total_time"])
        )
    sorted_data.reverse()

    ans = 0
    #logger.debug(f"sorted_data: {sorted_data}")
    values = [abs(item["total_time"]) for item in sorted_data]
    #logger.debug(f"values: {values}")
    for i  in range(len(values)):
        ans += (1 + i) * values[i]
 
    return ans