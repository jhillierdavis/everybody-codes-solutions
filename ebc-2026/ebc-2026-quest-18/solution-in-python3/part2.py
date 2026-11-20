from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common


def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    x_list = []
    y_list = []
    w_list = []
    for line in text.splitlines():
        #logger.debug(f"Looking at line: {line}")
        parts = line.split(" ")
        if len(parts) == 3:
            x_list.append(parts[0].removeprefix("x="))
            y_list.append(parts[1].removeprefix("y="))
            w_list.append(parts[2].removeprefix("width="))
    
    #logger.debug(f"x_list: {x_list}")
    #logger.debug(f"y_list: {y_list}")
    #logger.debug(f"w_list: {w_list}")

    x_max = max(map(int, x_list)) + 5
    y_max = max(map(int, y_list))

    #logger.debug(f"x_max: {x_max}")
    #logger.debug(f"y_max: {y_max}") 

    grid = [['.' for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x, y, w in zip(map(int, x_list), map(int, y_list), map(int, w_list)):
        for s in range(w):
            for i in range(y):
                grid[y_max - i][x + s] = '#'

    #for row in grid:
    #    logger.debug("".join(str(cell) for cell in row))

    
    grid = common.fill_horizontal(grid)

    #for row in grid:
    #    logger.debug("".join(str(cell) for cell in row))

    count = common.count_filled_cells(grid, x_max, y_max)
    return count