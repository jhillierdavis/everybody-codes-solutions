"""
Ref.: Based on core examples from: https://milkcrunch.com/aoc-core-skills/
"""

def to_grid(text):
    grid = [list(line) for line in text.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])    
    return grid, rows, cols


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