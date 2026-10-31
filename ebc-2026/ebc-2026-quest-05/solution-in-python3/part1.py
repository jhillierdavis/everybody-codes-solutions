import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from helpers import file_helper, grid_helper

def solve_part1(filename):
    text = file_helper.get_text(filename)

    grid, rows, cols = grid_helper.to_grid(text)

    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    logger.debug(f"rows: {rows}, cols: {cols}")

    land_grid = grid_helper.clone(grid)

    land_grid[rows//2][cols//2] = "#"
    logger.debug(f"Land Grid:\n{grid_helper.to_string(land_grid)}")

    for i in range(100):
        next_land_grid = grid_helper.clone(land_grid)
        land_cells = grid_helper.find_all(land_grid, '#')
        for lc in land_cells:
            neighbors = grid_helper.get_neighbor_positions(lc[0], lc[1], rows, cols, diagonals=True)
            for n in neighbors:
                values = grid_helper.get_neighbor_values(land_grid, n[0], n[1], rows, cols, diagonals=True)
                count = 0
                for v in values:
                    if v == '1' or v == '#':
                        count +=1
                if count >= 5:
                    next_land_grid[n[0]][n[1]] = '#'
        land_grid = next_land_grid
        #logger.debug(f"Land Grid:\n{grid_helper.to_string(land_grid)}")

    land_cells = grid_helper.find_all(land_grid, '#')
    return len(land_cells)