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

    quest_map = get_quest_map_from_input(text)
    #logger.debug(f"Quest map: {quest_map}")

    sorted_points = get_sorted_points(quest_map)

    ans = calculate_checksum(sorted_points)
    return ans


def get_quest_map_from_input(text):
    quest_map = defaultdict(list)
    for l in text.splitlines():
        #logger.debug(f"Processing line: {l}")
        parts = l.split()
        id = int(parts[0].split("=")[1])
        quest = int(parts[1].split("=")[1])
        part = int(parts[2].split("=")[1])
        time = int(parts[3].split("=")[1])

        # Append the quest data (user id, quest part & time taken to solve by user) to the quest map keyed by quest number
        quest_map[int(quest)].append({"id": id, "part": part, "time": time})

    return quest_map


def get_sorted_points(quest_map):

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
                            if points < 0:
                                points = 0 
                        same_value_count = 0
                points_map[item["id"]] += points
               
                logger.debug(f"Quest: {q} part: {p} id: {item['id']} gets points: {points} for time: {item['time']}")                   
                last_value = item["time"]

    #logger.debug(f"Points map: {points_map}")
    return sorted(points_map.items(), key=lambda x: x[1], reverse=True)


def calculate_checksum(sorted_points):
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