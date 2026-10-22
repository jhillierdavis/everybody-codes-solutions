"""
Ref.: Based on core examples from: https://milkcrunch.com/aoc-core-skills/
"""

def to_grid(text):
    grid = [list(line) for line in text.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])    
    return grid, rows, cols


def find_start(grid,start='S'):
    """Find the start (e.g. 'S') cell."""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == start:
                return (r, c)
    return None


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

def get_neighbors(r, c, rows, cols, directions=DIRECTIONS_4):
    """Return valid neighboring positions."""
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors