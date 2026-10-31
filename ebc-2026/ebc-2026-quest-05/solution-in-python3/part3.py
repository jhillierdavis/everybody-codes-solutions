from fileinput import filename
import logging
import logging.config
from turtle import distance

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from common import to_land, create_sand_for_land_perimeter, to_sand
from helpers import file_helper, grid_helper


def solve_part3(filename):
    text = file_helper.get_text(filename)

    grid, rows, cols = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    #logger.debug(f"rows: {rows}, cols: {cols}")

    land_grid = to_land(grid, rows, cols)
    perimeter_grid = create_sand_for_land_perimeter(land_grid, rows, cols)
    sand_grid = to_sand(perimeter_grid, rows, cols)

    tree_grid = plant_trees(sand_grid, rows, cols)
    for _ in range(2):
        tree_grid = grow_trees(tree_grid, rows, cols)
    

    #logger.debug(f"Tree Grid:\n{grid_helper.to_string(tree_grid)}")
    tree_cells = grid_helper.find_all(tree_grid, '@')
    return len(tree_cells)


def plant_trees(grid, rows, cols):
    land_cells = grid_helper.find_all(grid, '#')
    tree_grid = grid_helper.clone(grid)
    for lc in land_cells:
        distance = 2
        neighbors = get_neighbor_positions_up_to_distance(lc[0], lc[1], rows, cols, 2)
        excluded_neighbors = [(lc[0]-distance,lc[1]-distance), (lc[0]-distance,lc[1]+distance), (lc[0]+distance,lc[1]-distance), (lc[0]+distance,lc[1]+distance)]

        for e in excluded_neighbors:
            if e in neighbors:
                neighbors.remove(e)

        if all(grid[n[0]][n[1]] == '#' for n in neighbors):
            tree_grid[lc[0]][lc[1]] = '@'
    return tree_grid


def grow_trees(grid, rows, cols):
    land_cells = grid_helper.find_all(grid, '#')
    tree_grid = grid_helper.clone(grid)
    for lc in land_cells:
 
        neighbor_positions = grid_helper.get_neighbor_positions(lc[0], lc[1], rows, cols, diagonals=True)

        neigboring_tree_count = 0
        for n in neighbor_positions:
            if grid[n[0]][n[1]] == '=':
                neigboring_tree_count = 0
                break
            if grid[n[0]][n[1]] == '@':
                neigboring_tree_count += 1

        if neigboring_tree_count >= 4:
            tree_grid[lc[0]][lc[1]] = '@'

    return tree_grid


def get_neighbor_positions_up_to_distance(row, col, rows, cols, distance):
    """
    Return all valid neighboring cells within the specified distance.

    Args:
        row (int): Row index of the target cell.
        col (int): Column index of the target cell.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        distance (int): Maximum distance from the target cell.

    Returns:
        list[tuple[int, int]]: Neighboring cell coordinates.
    """
    neighbors = []

    for r in range(max(0, row - distance), min(rows, row + distance + 1)):
        for c in range(max(0, col - distance), min(cols, col + distance + 1)):
            if (r, c) != (row, col):  # exclude the center cell
                neighbors.append((r, c))

    return neighbors