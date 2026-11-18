import heapq

def shortest_path(grid, traversable='.'):
    """
    Implements Dijkstra's algorithm to find the shortest path from the top-left to the bottom-right of the grid.
    Only cells with the specified traversable character are considered passable.

    Arguments:
    - grid: 2D list representing the grid
    - traversable: character representing passable cells

    Returns:
    - Tuple of (distance, path) if a path exists, otherwise None
    """

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    pq = [(0, start)]          # (distance, node)
    dist = {start: 0}
    prev = {}

    directions = [
        (1, 0), (-1, 0),
        (0, 1), (0, -1)
    ]

    while pq:
        current_dist, (r, c) = heapq.heappop(pq)

        if (r, c) == goal:
            break

        if current_dist > dist[(r, c)]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == traversable
            ):
                nd = current_dist + 1

                if nd < dist.get((nr, nc), float('inf')):
                    dist[(nr, nc)] = nd
                    prev[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (nd, (nr, nc)))

    if goal not in dist:
        return None

    path = []
    node = goal

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()

    return dist[goal], path