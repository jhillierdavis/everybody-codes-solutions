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

def to_grid2d(text):
    grid, rows, cols = to_grid(text)
    return Grid2d(grid=grid, width=cols, height=rows)


def to_string(grid):
    str = ""

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            str += grid[r][c]
        str += '\n'
    return str


def clone(grid):
    grid_clone = [row[:] for row in grid]
    return grid_clone


def find_start(grid,start='S'):
    """Find the start (e.g. 'S') cell."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == start:
                return (r, c)
    return None

def add_border(grid, rows, cols, fill_value='.'):
    """Add a border around the grid with the specified fill value."""
    new_grid = [[fill_value] * (cols + 2)]
    for r in range(rows):
        new_grid.append([fill_value] + grid[r] + [fill_value])
    new_grid.append([fill_value] * (cols + 2))
    return new_grid, rows + 2, cols + 2

def find_all(grid, target):
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

def get_neighbor_positions(r, c, rows, cols, diagonals=False, wrap=False):
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


def get_neighbor_values(grid, r, c, rows, cols, diagonals=False, wrap=False):
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