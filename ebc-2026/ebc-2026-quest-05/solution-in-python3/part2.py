import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from common import to_land, create_sand_for_land_perimeter, to_sand
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
