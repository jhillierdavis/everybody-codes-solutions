from helpers import logging_helper, file_helper, grid_path_helper, grid_helper

logger = logging_helper.get_logger_instance()


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid = [list(line) for line in text.splitlines()]
    
    result = grid_path_helper.shortest_path(grid, '#')
    if result is not None:
        distance, path = result
        logger.debug(f"Distance: {distance}, Path: {path}")
        return distance 
    return -1
 