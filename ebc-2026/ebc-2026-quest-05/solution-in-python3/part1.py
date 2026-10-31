import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from helpers import file_helper, grid_helper
from common import to_land


def solve_part1(filename):
    text = file_helper.get_text(filename)

    grid, rows, cols = grid_helper.to_grid(text)

    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    logger.debug(f"rows: {rows}, cols: {cols}")

    land_grid = to_land(grid, rows, cols)

    land_cells = grid_helper.find_all(land_grid, '#')
    return len(land_cells)