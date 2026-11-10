from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

from collections import deque

def legacy_get_shortest_path(graph: dict[int, set[int]], start: int, end: int) -> list[int] | None:
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


def get_shortest_path(graph: dict[int, set[int]], start: int, end: int) -> list[int] | None:
    if start == end:
        return [start]

    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, ()):
            if neighbor in parent:
                continue

            parent[neighbor] = node

            if neighbor == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            queue.append(neighbor)

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