from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


from collections import defaultdict, deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def neighbours(r, c, rows, cols):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc


def find_all_paths(grid):
    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    paths = []

    def dfs(cell, path, visited):
        if cell == goal:
            paths.append(path.copy())
            return

        r, c = cell

        for nr, nc in neighbours(r, c, rows, cols):
            nxt = (nr, nc)

            if grid[nr][nc] != '#':
                continue

            if nxt in visited:
                continue

            visited.add(nxt)
            path.append(nxt)

            dfs(nxt, path, visited)

            path.pop()
            visited.remove(nxt)

    dfs(start, [start], {start})

    return paths


def outer_boundary_edges(cells):
    """
    Returns only edges that belong to the exterior boundary.
    """
    edges = defaultdict(int)

    for r, c in cells:

        sides = [
            ((c, r), (c + 1, r)),          # top
            ((c + 1, r), (c + 1, r + 1)), # right
            ((c, r + 1), (c + 1, r + 1)), # bottom
            ((c, r), (c, r + 1)),         # left
        ]

        for e in sides:
            e = tuple(sorted(e))
            edges[e] += 1

    # perimeter edges occur exactly once
    boundary = [e for e, n in edges.items() if n == 1]

    return boundary


def boundary_distance(path_cells):
    boundary = outer_boundary_edges(path_cells)

    graph = defaultdict(list)

    for a, b in boundary:
        graph[a].append(b)
        graph[b].append(a)

    start_corner = (0, 0)
    end_corner = (11, 6)  # bottom-right corner of goal cell

    q = deque([start_corner])
    dist = {start_corner: 0}

    while q:
        u = q.popleft()

        if u == end_corner:
            return dist[u]

        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)

    return None


def shortest_boundary_path(grid):
    best = float("inf")
    best_path = None

    for path in find_all_paths(grid):
        d = boundary_distance(set(path))

        if d is not None and d < best:
            best = d
            best_path = path

    return best, best_path


import part3_solver as solver

def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid = [list(line) for line in text.splitlines()]

    distance, path = shortest_boundary_path(grid)
    corner_path_info = solver.contour_side_lengths(grid)
    shortest_path = min(corner_path_info["north_east_path"], corner_path_info["south_west_path"])
    return shortest_path