from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

def build_circular_graph(node_count: int) -> dict[int, set[int]]:
    """Build the initial circular graph."""
    graph = {}

    for node in range(1, node_count + 1):
        neighbours = set()

        for offset in range(1, 4):
            neighbours.add(((node - 1 + offset) % node_count) + 1)
            neighbours.add(((node - 1 - offset) % node_count) + 1)

        graph[node] = neighbours

    return graph



def get_clock_value(value, max_value):
    return (value % max_value) or max_value


def pairings(values):
    values = list(values)

    if len(values) % 2 != 0:
        raise ValueError("Number of values must be even")

    def generate(remaining):
        if not remaining:
            return [set()]

        first = remaining[0]
        result = []

        for i in range(1, len(remaining)):
            second = remaining[i]

            pair = tuple(sorted((first, second)))
            rest = remaining[1:i] + remaining[i + 1:]

            for pairing in generate(rest):
                result.append(pairing | {pair})

        return result

    return generate(values)


import common
from copy import deepcopy

def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    sections = file_helper.get_text_sections(filename)
    portals = int(sections[0].split(" ")[1])
    logger.debug(f"Portals: {portals}")

    graph = build_circular_graph(portals)
    logger.debug(f"Graph: {graph}")

    initial_total_shortest_distances = common.get_total_shortest_distances(graph, portals) 
    logger.debug(f"Total shortest distances before processing shortcuts: {initial_total_shortest_distances}")

    for shortcuts in sections[1].splitlines():
        start, end = shortcuts.split(" ")
        start, end = int(start), int(end)
        logger.debug(f"Shortcut: Start: {start}, End: {end}")
        for i, v in graph.items():
            if i == start:
                v.add(end)
            if i == end:
                v.add(start)
    shortcuts_total_shortest_distances = common.get_total_shortest_distances(graph, portals)      
    logger.debug(f"Total shortest distances after processing shortcuts: {shortcuts_total_shortest_distances}")


    spacing = portals // 8
    logger.debug(f"Spacing: {spacing}")
    total_shortest_distances = set()


    for i in range(1, spacing + 1):
        spaced_nodes = set()
        for j in range(i, portals + 1, spacing):
            spaced_nodes.add(j)
        #logger.debug(f"Spaced nodes: {i}: {spaced_nodes}")

        graph_clone = {k: deepcopy(v) for k, v in graph.items()}
        pairings_list = pairings(spaced_nodes)
        for pairing in pairings_list:
            graph_clone = {k: deepcopy(v) for k, v in graph.items()}
            for x, y in pairing:
                graph_clone[x].add(y)
                graph_clone[y].add(x)
            spaced_total_shortest_distances = common.get_total_shortest_distances(graph_clone, portals)
            #logger.debug(f"Total shortest distances after processing spaced nodes {i}: {spaced_total_shortest_distances}")
            total_shortest_distances.add(spaced_total_shortest_distances)

    logger.debug(f"Total shortest distances for all spaced nodes: {total_shortest_distances}")
    min_value = min(total_shortest_distances)
    logger.debug(f"Minimum total shortest distances for all spaced nodes: {min_value}")
    return initial_total_shortest_distances - min_value