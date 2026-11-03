"""Helper functions for working with parent-child relationships"""

from collections import defaultdict, deque


def get_all_unique_descendent_references_for_parent(parent_child_map, parent, include_parent=False):   
    """
    Perform BFS (Breadth-First Search) to find all unique descendent (child, grandchild, etc.) references 
    for a given parent in the input key-value map (of parent key to direct child values).

    Args:
        parent_child_map (dict): A dictionary mapping parent keys to sets or lists of child values.
        parent: The parent key for which to find all descendent references.
        include_parent (bool): Whether to include the parent itself in the result.

    Returns:
        set: A set of all unique descendent references for the given parent.
    """
    visited = set()
    queue = [parent]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node in parent_child_map:
                for child in parent_child_map[node]:
                    if child != parent and child not in visited:
                        queue.append(child)
    if not include_parent and parent in visited:
        visited.remove(parent)
    return visited


def get_all_unique_ancestors_of_child(parent_child_map, target_child, include_target_child=False):
    """
    Find all parent keys that directly or indirectly have target_child as a child.
    
    Args:
        parent_child_map (dict): A dictionary mapping parent keys to sets or lists of child values.
        target_child: The child value for which to find all ancestor parents.
        include_target_child (bool): Whether to include the target child itself in the result.

    Returns:
        set: A set of all unique ancestor parent keys for the target child.
    """

    # Keys that directly contain the value
    result = {
        key
        for key, values in parent_child_map.items()
        if target_child in values
    }

    # Reverse graph: child -> parents
    parents = defaultdict(set)

    for parent, values in parent_child_map.items():
        for value in values:
            if value in parent_child_map:  # value is also a key
                parents[value].add(parent)

    # Traverse upward to find indirect containers
    queue = deque(result)

    while queue:
        current = queue.popleft()

        for parent in parents[current]:
            if parent not in result:
                result.add(parent)
                queue.append(parent)
    
    if not include_target_child and target_child in result:
        result.remove(target_child)
    
    return result