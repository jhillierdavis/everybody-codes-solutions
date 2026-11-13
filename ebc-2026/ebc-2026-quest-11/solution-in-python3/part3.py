from copy import deepcopy

from helpers import logging_helper, file_helper
from helpers.graph_helper import generate_circular_graph
from helpers.pairing_helper import get_unique_pairings

logger = logging_helper.get_logger_instance()

import common

def solve_part3(filename):
    #text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    sections = file_helper.get_text_sections(filename)
    portals = int(sections[0].split(" ")[1])
    logger.debug(f"Portals: {portals}")

    graph = generate_circular_graph(portals, 3)
    logger.debug(f"Graph: {graph}")

    initial_total_shortest_distances = common.get_total_shortest_distances(graph, portals) 
    logger.debug(f"Total shortest distances before processing shortcuts: {initial_total_shortest_distances}")

    # Process additional shortcuts between pairs of nodes
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

    # Determine the even spacing of 8 special 'crystal' nodes
    spacing = portals // 8
    logger.debug(f"Spacing: {spacing}")
    total_shortest_distances = set()

    # Arrange pair of 'crystal' nodes with even spacing for minimal 'portal strain' (total shortest distance between nodes) value
    for i in range(1, spacing + 1):
        spaced_nodes = set()
        for j in range(i, portals + 1, spacing):
            spaced_nodes.add(j)
        #logger.debug(f"Spaced nodes: {i}: {spaced_nodes}")

        graph_clone = {k: deepcopy(v) for k, v in graph.items()}
        pairings_list = get_unique_pairings(spaced_nodes)
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