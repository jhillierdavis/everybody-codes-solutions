from helpers import logging_helper, file_helper, grid_path_helper, grid_helper

logger = logging_helper.get_logger_instance()


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid = [list(line) for line in text.splitlines()]

    start = (0,0)
    finish = (len(grid) - 1, len(grid[0]) - 1)
    
    result = grid_path_helper.shortest_path(grid, start, finish, traversable='#')
    if result is not None:
        distance, path = result
        logger.debug(f"Distance: {distance}, Path: {path}")
        return distance 
    return -1
 