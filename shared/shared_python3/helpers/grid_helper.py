"""
Ref.: Initially based on core examples from: https://milkcrunch.com/aoc-core-skills/
"""

from collections import deque
from dataclasses import dataclass
from warnings import deprecated

@dataclass(frozen=True)
class Grid2d:
    grid: list[list]
    width: int
    height: int

# def deprecated(message):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             import warnings
#             warnings.warn(message, DeprecationWarning, stacklevel=2)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

@deprecated("Use to_grid2d instead")
def to_grid(text):
    grid = [list(line) for line in text.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])    
    return grid, rows, cols


def to_grid2d(text: str) -> Grid2d:
    grid = [list(line) for line in text.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])
    return Grid2d(grid=grid, width=cols, height=rows)


def to_string(grid: list[list]) -> str:
    str = ""

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            str += grid[r][c]
        str += '\n'
    return str


def clone(grid: list[list]) -> list[list]:
    grid_clone = [row[:] for row in grid]
    return grid_clone


def find_start(grid: list[list], start: str = 'S') -> tuple[int, int] | None:
    """Find the start (e.g. 'S') cell."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == start:
                return (r, c)
    return None


def add_border(grid: list[list], rows: int, cols: int, fill_value: str = '.') -> tuple[list[list], int, int]:
    """Add a border around the grid with the specified fill value."""
    new_grid = [[fill_value] * (cols + 2)]
    for r in range(rows):
        new_grid.append([fill_value] + grid[r] + [fill_value])
    new_grid.append([fill_value] * (cols + 2))
    return new_grid, rows + 2, cols + 2


def find_all(grid: list[list], target: str) -> list[tuple[int, int]]:
    """Find all cells matching target."""
    positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                positions.append((r, c))
    return positions


# Four cardinal directions (up, down, left, right)
DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Eight directions (including diagonals)
DIRECTIONS_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def get_neighbor_positions(r: int, c: int, rows: int, cols: int, diagonals: bool = False, wrap: bool = False) -> list[tuple[int, int]]:
    """Return valid neighboring positions."""
    neighbors = []
    for dr, dc in DIRECTIONS_8 if diagonals else DIRECTIONS_4:
        nr, nc = r + dr, c + dc
        if wrap:
            nr %= rows
            nc %= cols
            neighbors.append((nr, nc))
        else:
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
    return neighbors


def get_neighbor_values(grid: list[list], r: int, c: int, rows: int, cols: int, diagonals: bool = False, wrap: bool = False) -> list:
    """Return the values of valid neighboring cells."""
    positions = get_neighbor_positions(r, c, rows, cols, diagonals, wrap)
    return [grid[r][c] for r, c in positions]


def minimum_segment_cover(grid: list[str], target: str = "#") -> int:
    """
    Returns the minimum number of horizontal/vertical segments 
    (lines or 'rays') required to erase all '#' cells.

    A line may erase exactly one maximal contiguous horizontal
    or vertical run of '#' (default behavior).

    Computes the minimum number of horizontal and vertical
    contiguous segments (lines) required to cover every occupied
    ('#') cell in the grid.

    Implemented by reducing the problem to a minimum
    vertex cover in a bipartite graph and solving via
    Hopcroft-Karp maximum matching.
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    #
    # Step 1:
    # Assign an id to every maximal horizontal run.
    #
    horizontal_id = {}
    horizontal_count = 0

    for y in range(rows):

        x = 0

        while x < cols:

            if grid[y][x] != target:
                x += 1
                continue

            run_id = horizontal_count
            horizontal_count += 1

            while x < cols and grid[y][x] == target:
                horizontal_id[(y, x)] = run_id
                x += 1

    #
    # Step 2:
    # Assign an id to every maximal vertical run.
    #
    vertical_id = {}
    vertical_count = 0

    for x in range(cols):

        y = 0

        while y < rows:

            if grid[y][x] != target:
                y += 1
                continue

            run_id = vertical_count
            vertical_count += 1

            while y < rows and grid[y][x] == target:
                vertical_id[(y, x)] = run_id
                y += 1

    #
    # Step 3:
    # Build bipartite graph.
    #
    graph = [set() for _ in range(horizontal_count)]

    for cell, h in horizontal_id.items():
        v = vertical_id[cell]
        graph[h].add(v)

    #
    # Step 4:
    # Hopcroft-Karp maximum matching.
    #
    INF = float("inf")

    pair_u = [-1] * horizontal_count
    pair_v = [-1] * vertical_count
    dist = [0] * horizontal_count

    def bfs():

        queue = deque()

        for u in range(horizontal_count):

            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        found_augmenting_path = False

        while queue:

            u = queue.popleft()

            for v in graph[u]:

                matched_u = pair_v[v]

                if matched_u == -1:
                    found_augmenting_path = True

                elif dist[matched_u] == INF:
                    dist[matched_u] = dist[u] + 1
                    queue.append(matched_u)

        return found_augmenting_path

    def dfs(u):

        for v in graph[u]:

            matched_u = pair_v[v]

            if matched_u == -1 or (
                dist[matched_u] == dist[u] + 1
                and dfs(matched_u)
            ):

                pair_u[u] = v
                pair_v[v] = u

                return True

        dist[u] = INF
        return False

    matching = 0

    while bfs():

        for u in range(horizontal_count):

            if pair_u[u] == -1 and dfs(u):
                matching += 1

    #
    # By König's theorem:
    # minimum vertex cover size == maximum matching size
    #
    return matching


def find_shortest_path_with_waypoints(grid, start_symbol='S', end_symbol='E', wall_symbol='#', waypoint_symbol='@'):
    rows = len(grid)
    cols = len(grid[0])

    start = None
    end = None
    waypoints = []

    # Locate S, E and all @
    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch == start_symbol:
                start = (r, c)
            elif ch == end_symbol:
                end = (r, c)
            elif ch == waypoint_symbol:
                waypoints.append((r, c))

    if start is None or end is None:
        raise ValueError("Grid must contain S and E")

    waypoint_index = {
        pos: i for i, pos in enumerate(waypoints)
    }

    all_waypoints_mask = (1 << len(waypoints)) - 1

    # State:
    # (row, col, visited_waypoint_mask, previous_position)
    start_state = (
        start[0],
        start[1],
        0,
        None
    )

    queue = deque([start_state])

    visited = {start_state}
    parent = {start_state: None}

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while queue:
        r, c, mask, prev = queue.popleft()

        # Mark waypoint visited if standing on one
        if (r, c) in waypoint_index:
            mask |= (1 << waypoint_index[(r, c)])

        current_state = (r, c, mask, prev)

        # Goal reached?
        if (r, c) == end and mask == all_waypoints_mask:
            path = []

            state = current_state
            while state is not None:
                path.append((state[0], state[1]))
                state = parent[state]

            path.reverse()
            return path

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            if grid[nr][nc] == wall_symbol:
                continue

            # No immediate backtracking
            if prev is not None and (nr, nc) == prev:
                continue

            next_prev = (r, c)

            next_mask = mask
            if (nr, nc) in waypoint_index:
                next_mask |= (1 << waypoint_index[(nr, nc)])

            next_state = (
                nr,
                nc,
                next_mask,
                next_prev
            )

            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current_state
                queue.append(next_state)

    return None


def print_path(grid, path):
    if path is None:
        print("No valid path found")
        return

    display = [list(row) for row in grid]

    for r, c in path:
        if display[r][c] == '.':
            display[r][c] = '*'

    for row in display:
        print("".join(row))

    print("\nPath length:", len(path) - 1)
    print("Path:", path)