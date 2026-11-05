from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def calcuate_grid_energy(grid, rows, cols):
    total_energy = 0
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                total_energy += int(value)
    return total_energy

def count_trees(grid, rows, cols):
    tree_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                tree_count += 1
    return tree_count

def get_next_diagonal_position(rows, cols, r, c):
    next_r = r + 1
    next_c = c + 1
    if next_r < rows and next_c < cols:
        return next_r, next_c
    return None


def process_tree_line(shaded_grid, rows, cols, r, c, num):
    for x in range(1, num):
        next_pos = get_next_diagonal_position(rows, cols, r, c)
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


def get_shaded_grid(grid, rows, cols):
    shaded_grid = grid_helper.clone(grid)
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value != '.':
                num = int(value)
                process_tree_line(shaded_grid, rows, cols, r, c, num)
    return shaded_grid


def solve_part1(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")

    shaded_grid = get_shaded_grid(grid, rows, cols)
    #logger.debug(f"Shaded Grid:\n{grid_helper.to_string(shaded_grid)}")

    return count_trees(shaded_grid, rows, cols)