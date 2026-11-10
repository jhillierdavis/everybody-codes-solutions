from helpers import logging_helper, file_helper
import common

logger = logging_helper.get_logger_instance()

def get_clock_value(value, max_value):
    return (value % max_value) or max_value

from copy import deepcopy

def solve_part2(filename):
    #text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    sections = file_helper.get_text_sections(filename)
    portals = int(sections[0].split(" ")[1])
    logger.debug(f"Portals: {portals}")

    """
    map = {}
    for i in range(1, portals+1):
        neighbours = set()
        if i == 1:
            neighbours = {i+1, i+2, i+3, portals, portals-1, portals-2}
        elif i == 2:
            neighbours = {i+1, i+2, i+3, i-1, portals, portals-1}
        elif i == 3:
            neighbours = {i+1, i+2, i+3, i-1, i-2, portals}
        elif i == portals:
            neighbours = {1, 2, 3, i-1, i-2, i-3}            
        elif i == portals-1:
            neighbours = {portals, 1, 2, i-1, i-2, i-3}
        elif i == portals-2:
            neighbours = {portals-1, portals, 1, i-1, i-2, i-3}
        else:
            neighbours = {i+1, i+2, i+3, i-1, i-2, i-3}
        map[i] = neighbours
    """
    map = {}
    for i in range(1, portals+1):
        neighbours = {get_clock_value(i+1, portals), get_clock_value(i+2, portals), get_clock_value(i+3, portals), get_clock_value(i-1, portals), get_clock_value(i-2, portals), get_clock_value(i-3, portals)}
        map[i] = neighbours
    logger.debug(f"Map: {map}")

    initial_total_shortest_distances = common.get_total_shortest_distances(map, portals)
    logger.debug(f"Total shortest distances before processing shortcuts: {initial_total_shortest_distances}")

    for shortcuts in sections[1].splitlines():
        start, end = shortcuts.split(" ")
        start, end = int(start), int(end)
        logger.debug(f"Shortcut: Start: {start}, End: {end}")
        for i, v in map.items():
            if i == start:
                v.add(end)
            if i == end:
                v.add(start)
    shortcuts_total_shortest_distances = common.get_total_shortest_distances(map, portals)      
    logger.debug(f"Total shortest distances after processing shortcuts: {shortcuts_total_shortest_distances}")

    total_shortcut_distances = set()
    #total_shortcut_distances.add(shortcuts_total_shortest_distances)
    for i in range(1, portals+1):       
        for j in range(1, portals+1):
            #map_clone = map.copy()
            map_clone = deepcopy(map)
            map_clone = {k: deepcopy(v) for k, v in map.items()}
            if i != j and j not in map_clone[i] and i not in map_clone[j]:
                    map_clone[i].add(j)
                    map_clone[j].add(i)
                    shortcuts_total_shortest_distances = common.get_total_shortest_distances(map_clone, portals)
                    logger.debug(f"Total shortest distances with shortcut {i}-{j}: {shortcuts_total_shortest_distances}")
                    total_shortcut_distances.add(shortcuts_total_shortest_distances)

    logger.debug(f"Total shortest distances with all possible shortcuts: {sorted(total_shortcut_distances)}")
    max_value = max(total_shortcut_distances)
    logger.debug(f"Maximum total shortest distances with a single shortcut: {max_value}")
    return initial_total_shortest_distances - max_value
