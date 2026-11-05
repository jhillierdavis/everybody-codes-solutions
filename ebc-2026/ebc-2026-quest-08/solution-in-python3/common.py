
from helpers import logging_helper

logger = logging_helper.get_logger_instance()

def count_trees(grid, rows, cols):
    tree_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                tree_count += 1
    return tree_count


def get_next_position_south_east(rows, cols, r, c):
    next_r = r + 1
    next_c = c + 1
    if next_r < rows and next_c < cols:
        return next_r, next_c
    return None


def process_tree_line_south_east(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_position_south_east(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c    


def get_next_position_south_west(rows, cols, r, c):
    next_r = r + 1
    next_c = c - 1
    if next_r < rows and next_c >= 0:
        return next_r, next_c
    return None


def process_tree_line_south_west(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_position_south_west(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c


def get_next_position_west(rows, cols, r, c):
    next_r = r
    next_c = c - 2
    if next_c >= 0:
        return next_r, next_c
    return None


def process_tree_line_west(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_position_west(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c  


def get_next_position_north_west(rows, cols, r, c):
    next_r = r - 1
    next_c = c - 1
    if next_r >= 0 and next_c >= 0:
        return next_r, next_c
    return None


def process_tree_line_north_west(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_position_north_west(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c  


def get_next_position_north_east(rows, cols, r, c):
    next_r = r - 1
    next_c = c + 1
    if next_r >= 0 and next_c < cols:
        return next_r, next_c
    return None


def process_tree_line_north_east(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_position_north_east(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c  


def get_next_position_east(rows, cols, r, c):
    next_r = r
    next_c = c + 2
    if next_c < cols:
        return next_r, next_c
    return None


def process_tree_line_east(shaded_grid, rows, cols, r, c, num):
    #logger.debug(f"Processing east of tree at ({r}, {c}) with value {shaded_grid[r][c]} num={num}")
    for x in range(1, num):
        next_pos = get_next_position_east(rows, cols, r, c)
        if next_pos is None:
            break
        next_r, next_c = next_pos
        next_value = shaded_grid[next_r][next_c]
        if next_value != '.':
            next_num = int(next_value)
            #logger.debug(f"Processing subsequent tree at ({next_r}, {next_c}) with value {next_value} num={num} x={x} shade={num-x}")
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_grid[next_r][next_c] = '.'
        r, c = next_r, next_c 