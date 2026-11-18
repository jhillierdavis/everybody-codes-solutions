from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def solve_part2(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)
    grid = grid2d.grid
    logger.debug(f"Grid2d: {grid2d}")

    #logger.debug(f"Grid position info: {grid[4][0]}")
    #logger.debug(f"Grid position info: {grid[6][0]}")
    #logger.debug(f"Grid position info: {grid[5][1]}")
    
    count = 0
    height = grid2d.height
    width = grid2d.width
    for r in range(height):
        for c in range(width):
            if grid[r][c] == '#':
                sides = 4
                nvs = grid_helper.get_neighbor_values(grid, r, c, height, width)
                for nv in nvs:
                    if nv == '#':
                        # Do something with each neighbouring '#' cell
                        sides -= 1
                count += sides
    
    return count