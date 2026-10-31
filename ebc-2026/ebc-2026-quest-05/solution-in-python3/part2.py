import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from common import to_land
from helpers import file_helper, grid_helper


def solve_part2(filename):
    text = file_helper.get_text(filename)

    grid, rows, cols = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    #logger.debug(f"rows: {rows}, cols: {cols}")

    land_grid = to_land(grid, rows, cols)
    perimeter_grid = create_sand_for_land_perimeter(land_grid, rows, cols)
    sand_grid = to_sand(perimeter_grid, rows, cols)
    sand_cells = grid_helper.find_all(sand_grid, '=')
    return len(sand_cells)


def create_sand_for_land_perimeter(grid, rows, cols):
    land_grid = grid_helper.clone(grid)

    perimeter_grid = grid_helper.clone(land_grid)
    land_cells = grid_helper.find_all(land_grid, '#')
    for lc in land_cells:
        values = grid_helper.get_neighbor_values(land_grid, lc[0], lc[1], rows, cols, diagonals=True)
        count = 0
        for v in values:
            if v == '#':
                count +=1
        if count < 8:
            perimeter_grid[lc[0]][lc[1]] = '='
    #logger.debug(f"Perimeter Grid:\n{grid_helper.to_string(perimeter_grid)}")
    return perimeter_grid


def to_sand(grid, rows, cols):
    land_grid = grid_helper.clone(grid)    
    is_changed = True
    while is_changed:
        is_changed = False
        next_land_grid = grid_helper.clone(land_grid)
        land_cells = grid_helper.find_all(land_grid, '#')
        for lc in land_cells:
            neighbors = grid_helper.get_neighbor_positions(lc[0], lc[1], rows, cols, diagonals=True)
            for n in neighbors:
                values = grid_helper.get_neighbor_values(land_grid, n[0], n[1], rows, cols, diagonals=True)
                count = 0
                for v in values:
                    if v == '=':
                        count +=1
                if count >= 5 and land_grid[n[0]][n[1]] != '=':
                    next_land_grid[n[0]][n[1]] = '='
                    is_changed = True
        land_grid = next_land_grid
        #logger.debug(f"Land Grid:\n{grid_helper.to_string(land_grid)}")``
    return land_grid