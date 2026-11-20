from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


import common


def solve_part1(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    x_list = []
    y_list = []
    for line in text.splitlines():
        logger.debug(f"Looking at line: {line}")
        parts = line.split(" ")
        if len(parts) == 2:
            x_list.append(parts[0].removeprefix("x="))
            y_list.append(parts[1].removeprefix("y="))
    
    logger.debug(f"x_list: {x_list}")
    logger.debug(f"y_list: {y_list}")

    x_max = max(map(int, x_list))
    y_max = max(map(int, y_list))

    logger.debug(f"x_max: {x_max}")
    logger.debug(f"y_max: {y_max}") 

    grid = [['.' for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x, y in zip(map(int, x_list), map(int, y_list)):
        for i in range(y):
            grid[y_max - i][x] = '#'

    #for row in grid:
    #    logger.debug("".join(str(cell) for cell in row))

    grid = common.fill_horizontal(grid)

    #for row in grid:
    #    logger.debug("".join(str(cell) for cell in row))

    count = common.count_filled_cells(grid, x_max, y_max)
    return count