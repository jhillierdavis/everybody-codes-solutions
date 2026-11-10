from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

from collections import deque

def get_shortest_path(graph: dict[int, set[int]], start: int, end: int) -> list[int] | None:
    """
    Find the shortest path between start and end in an unweighted graph.

    Args:
        graph: Maps each node to a collection of neighboring nodes.
        start: Starting node.
        end: Target node.

    Returns:
        List of nodes representing the shortest path, or None if no path exists.
    """
    if start == end:
        return [start]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, ()):
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def get_total_shortest_distances(map: dict[int, set[int]], portals: int) -> int:
    total_distance = 0
    for i in range(1, portals+1):
        total_distance += get_shortest_distances(map, i, portals)
    return total_distance


def get_shortest_distances(map: dict[int, set[int]], start: int, portals: int) -> int:
    distance = 0
    for i in range(1, portals+1):
        shortest_path = get_shortest_path(map, start, i)
        #logger.debug(f"Shortest path from {start} to {i}: {shortest_path}")
        if shortest_path is not None:
            distance += len(shortest_path) - 1    
    return distance


def solve_part1(filename):
    #text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    sections = file_helper.get_text_sections(filename)
    portals = int(sections[0].split(" ")[1])
    logger.debug(f"Portals: {portals}")

    map = {}
    for i in range(1, portals+1):
        neighbours = set()
        if i == 1:
            neighbours = {i+1, portals}
        elif i == portals:
            neighbours = {1, i-1}
        else:
            neighbours = {i+1, i-1}
        map[i] = neighbours

    logger.debug(f"Map: {map}")
    
    # Process shortcuts
    #logger.debug(f"Sections[0]: {sections[0]}")

    initial_total_shortest_distances = get_total_shortest_distances(map, portals)
    logger.debug(f"Total shortest distances before processing shortcuts: {initial_total_shortest_distances}")

    #shortcuts = sections[1].splitlines()
    #logger.debug(f"Shortcuts: {shortcuts}")

    for shortcuts in sections[1].splitlines():
        start, end = shortcuts.split(" ")
        start, end = int(start), int(end)
        logger.debug(f"Shortcut: Start: {start}, End: {end}")
        for i, v in map.items():
            if i == start:
                v.add(end)
            if i == end:
                v.add(start)

    shortcuts_total_shortest_distances = get_total_shortest_distances(map, portals)
    logger.debug(f"Total shortest distances after processing shortcuts: {shortcuts_total_shortest_distances}")

    #logger.debug(f"Sections[1]: {sections[1]}")
    """
    for shortcut in sections[1]:
        logger.debug(f"Processing shortcut: {shortcut}")
        start, end = map(int, shortcut.split())
        logger.debug(f"Start: {start}, End: {end}")
        shortest_path = get_shortest_path(map, start, end)
        logger.debug(f"Shortest path for shortcut from {start} to {end}: {shortest_path}")
        if shortest_path is not None:
            total_distance += len(shortest_path) - 1
        logger.debug(f"Total distance after processing shortcut from {start} to {end}: {total_distance}")
    """
    return initial_total_shortest_distances - shortcuts_total_shortest_distances