from itertools import count

from helpers import logging_helper, file_helper, grid_helper
import common

logger = logging_helper.get_logger_instance()


def get_shaded_trees_to_south_east(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_south_east)

def get_shaded_trees_to_south_west(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_south_west)   

def get_shaded_trees_to_north_west(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_north_west)

def get_shaded_trees_to_north_east(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_north_east)

def get_shaded_trees_to_east(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_east)

def get_shaded_trees_to_west(shaded_grid, rows, cols, r, c, num):
    return get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, common.get_next_position_west)

def get_shaded_trees_in_direction(shaded_grid, rows, cols, r, c, num, direction_function):
    shaded_trees = set()
    for x in range(1, num):
        next_pos = direction_function(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_trees.add((next_r, next_c))
        r, c = next_r, next_c 
    return shaded_trees


def count_unshaded_trees_to_south_east(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_south_east)

def count_unshaded_trees_to_south_west(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_south_west)

def count_unshaded_trees_to_north_east(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_north_east)

def count_unshaded_trees_to_north_west(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_north_west)

def count_unshaded_trees_to_west(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_west)
    
def count_unshaded_trees_to_east(filename):
    return count_unshaded_trees_in_direction(filename, get_shaded_trees_to_east)


def count_unshaded_trees_in_direction(filename, direction_function):
    text = file_helper.get_text(filename)
    grid, rows, cols = grid_helper.to_grid(text)
    #for r in range(rows-1, 0, -1):
    shaded_trees = set()
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                shaded_trees.update(direction_function(grid, rows, cols, r, c, num))

    unshaded_grid = grid_helper.clone(grid)
    for r, c in shaded_trees:
        unshaded_grid[r][c] = '.'
    return common.count_trees(unshaded_grid, rows, cols)

"""
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
"""

def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")

    ans = 0

    value = count_unshaded_trees_to_south_east(filename)
    #logger.debug(f"Shaded Grid South East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid South East: value={value}")
    ans += value

    value = count_unshaded_trees_to_south_west(filename)
    #logger.debug(f"Shaded Grid South West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid South West: value={value}")
    ans += value
    
    value = count_unshaded_trees_to_west(filename)
    #logger.debug(f"Shaded Grid West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid West: value={value}")
    ans += value

    value = count_unshaded_trees_to_north_west(filename)
    #logger.debug(f"Shaded Grid North West: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid North West: value={value}")
    ans += value
    
    value = count_unshaded_trees_to_north_east(filename)
    #logger.debug(f"Shaded Grid North East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid North East: value={value}")
    ans += value
    
    value = count_unshaded_trees_to_east(filename)
    #logger.debug(f"Shaded Grid East: shaded_grid=\n{grid_helper.to_string(shaded_grid)}")
    logger.debug(f"Shaded Grid East: value={value}")
    ans += value

    return ans