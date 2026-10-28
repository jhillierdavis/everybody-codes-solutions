import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def to_precedence_graph(input, separator=' '):
    """
    Convert input string into a precedence graph.
    The input string should contain edges in the form "A<B" or "A>B" indicating that A is smaller or larger than B, respectively.

    Args:
        input (str): Input string containing edges separated by the separator.
        separator (str): Separator used to split edges in the input string.

    Returns:
        dict: A dictionary representing the precedence graph where keys are nodes and values are sets of (larger) dependencies.
    """
    edges = input.split(separator)
    graph = {}
    for edge in edges:
        a, b = edge.split('<') if '<' in edge else edge.split('>')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        if '<' in edge: # Map smaller node to larger node as dependency
            graph[b].add(a)
        else:
            graph[a].add(b)

    logger.debug(f"graph={graph} input={input}")    
    return graph


def get_nodes_by_precedence(input, separator=' ', smallest_first=True):
    """
    Get nodes from the precedence graph in order of precedence.

    Args:
        input (str): Input string containing edges separated by the separator.
        separator (str): Separator used to split edges in the input string.
        smallest_first (bool): If True, return nodes from smallest to largest. If False, return nodes from largest to smallest.

    Returns:
        list: A list of nodes ordered by precedence.
    """
    graph = to_precedence_graph(input, separator)

    result = []
    while graph:
        is_changed = False
        for node, deps in graph.items():
            if not deps:
                result.append(node) # Append node with no larger dependencies to result
                del graph[node] # Remove node from graph as it has no larger dependencies
                for n in graph: # Remove the node from the larger dependency set of other nodes
                    graph[n].discard(node)
                logger.debug(f"Node without dependencies: node={node} graph={graph} result={result}")
                is_changed = True
                break
        if not is_changed:
            logger.debug(f"No changes in this iteration, graph={graph} result={result}")
            raise RuntimeError("Cyclic dependency detected in the graph.")
        
    if not smallest_first:
        result.reverse()
    return result


def get_nodes_by_precedence_largest_first(input, separator=' '):
    return get_nodes_by_precedence(input, separator, smallest_first=False)