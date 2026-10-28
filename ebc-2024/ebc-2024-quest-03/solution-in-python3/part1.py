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
    str_grid = grid_helper.to_string(grid)
    
    logger.debug(f"Grid read from file {filename}: \n{str_grid}")

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                grid[r][c] = '1'

    logger.debug(f"Grid: \n{grid_helper.to_string(grid)}")

    
    last_grid = grid_helper.clone(grid)
    for i in range(1,100):
        next_grid = grid_helper.clone(last_grid)
        for r in range(rows):
                for c in range(cols):
                    neighbors = grid_helper.get_neighbor_values(last_grid, r, c, rows, cols)
                    value = str(i)
                    next_value = str(i+1)
                    if all(n == value for n in neighbors):
                        next_grid[r][c] = next_value
                        is_changed = True

        logger.debug(f"Grid: \n{grid_helper.to_string(next_grid)}")
        if not is_changed:
            logger.debug(f"No changes in iteration {i}, stopping early.")
            break
        last_grid = next_grid


    ans = 0
    for r in range(rows):
        for c in range(cols):
            value = last_grid[r][c]
            if value.isdigit():
                ans += int(value)

    return ans