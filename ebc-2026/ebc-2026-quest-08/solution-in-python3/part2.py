from helpers import logging_helper, file_helper, grid_helper
import common

logger = logging_helper.get_logger_instance()


def get_grid_shaded_south_east(grid, rows, cols):
    #for r in range(rows-1, 0, -1):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                common.process_tree_line_south_east(grid, rows, cols, r, c, num)
    return grid

def get_grid_shaded_south_west(grid, rows, cols):
    #for r in range(rows-1, 0, -1):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                common.process_tree_line_south_west(grid, rows, cols, r, c, num)
    return grid

def get_grid_shaded_west(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                common.process_tree_line_west(grid, rows, cols, r, c, num)
    return grid

def get_grid_shaded_north_west(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                common.process_tree_line_north_west(grid, rows, cols, r, c, num)
    return grid


def get_grid_shaded_north_east(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                common.process_tree_line_north_east(grid, rows, cols, r, c, num)
    return grid


def get_grid_shaded_east(grid, rows, cols):
    for r in range(rows):
        for c in range(cols-1,0,-1):
        #for c in range(cols):
            value = grid[r][c]
            if value != '.':
                #logger.debug(f"Processing tree at ({r}, {c}) with value {value}")
                num = int(value)
                common.process_tree_line_east(grid, rows, cols, r, c, num)
    return grid


def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")

    

    ans = 0
    
    shaded_grid = grid_helper.clone(grid)
    shaded_grid = get_grid_shaded_south_east(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid South East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid South East: value={value}")
    ans += value

    shaded_grid = grid_helper.clone(grid)
    shaded_grid = get_grid_shaded_south_west(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid South West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid South West: value={value}")
    ans += value
    
    shaded_grid = get_grid_shaded_west(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid West: value={value}")
    ans += value

    shaded_grid = grid_helper.clone(grid)
    shaded_grid = get_grid_shaded_north_west(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid North West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid North West: value={value}")
    ans += value
    
    shaded_grid = grid_helper.clone(grid)
    shaded_grid = get_grid_shaded_north_east(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid North East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid North East: value={value}")
    ans += value
    
    shaded_grid = grid_helper.clone(grid)
    shaded_grid = get_grid_shaded_east(shaded_grid, rows, cols)
    value = common.count_trees(shaded_grid, rows, cols)
    #logger.debug(f"Shaded Grid East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid East: value={value}")
    ans += value

    return ans