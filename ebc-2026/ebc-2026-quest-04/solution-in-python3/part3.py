import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from collections import defaultdict
from helpers import file_helper


def solve_part3(filename):
    text = file_helper.get_text(filename)

    data = []
    quest_map = defaultdict(list)
    for l in text.splitlines():
        #logger.debug(f"Processing line: {l}")
        parts = l.split()
        id = parts[0].split("=")[1]
        quest = parts[1].split("=")[1]
        part = parts[2].split("=")[1]
        time = int(parts[3].split("=")[1])
        data.append({"id": int(id), "quest": int(quest), "part": int(part), "time": int(time)})        
        quest_map[int(quest)].append({"id": int(id), "part": int(part), "time": int(time)})

    #logger.debug(f"Processed data: {data}")
    #logger.debug(f"Quest map: {quest_map}")

    points_map = defaultdict(int)
    for q, v  in quest_map.items():
        logger.debug(f"Quest {q} has values: {v}")
        part_map = defaultdict(list)
        for item in v:
            part_map[item["part"]].append(item)
        #logger.debug(f"Quest {q} has part map: {part_map}")

        for p in part_map:
            part_data = []
            for v in part_map[p]:
                combined_time =  int(v["time"])
                if p == 2 or p == 3:
                    combined_time += sum(item["time"] for item in quest_map[q] if item["part"] == 1 and item["id"] == v["id"])
                if p == 3:
                    combined_time += sum(item["time"] for item in quest_map[q] if item["part"] == 2 and item["id"] == v["id"])
                part_data.append({"id": int(v["id"]), "time": combined_time})

            part_data.sort(key=lambda x: x["time"])
            logger.debug(f"Quest {q} part {p} has sorted part data: {part_data}")

            points = 50 if p == 1 else (100 if p == 2 else 150)
            last_value = None
            same_value_count = 0
            for i, item in enumerate(part_data):
                if last_value is not None:
                    if item["time"] == last_value:
                        same_value_count += 1
                    else:
                        if points > 0:
                            points -= (1 + same_value_count) 
                        same_value_count = 0
                points_map[item["id"]] += points
               
                logger.debug(f"Quest: {q} part: {p} id: {item['id']} gets points: {points} for time: {item['time']}")                   
                last_value = item["time"]


    #logger.debug(f"Points map: {points_map}")

    sorted_points = sorted(points_map.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    last_points = None
    same_points_count = 0
    for i, (id, points) in enumerate(sorted_points):
        index = i + 1
        logger.debug(f"index: {index} id: {id} has total points: {points}")
        if last_points is not None and points == last_points:
            same_points_count += 1
            ans += (index - same_points_count) * points
            logger.debug(f"Tie: index: {index} id: {id} has total points: {points} (same as previous, same_points_count: {same_points_count})")
        else:
            same_points_count = 0
            ans += index * points
        last_points = points
    return ans