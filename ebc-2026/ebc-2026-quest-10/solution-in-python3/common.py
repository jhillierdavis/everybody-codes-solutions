from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def get_wall_positions(grid, rows, cols):
    wall_positions = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                wall_positions.add((r,c))
    return wall_positions


def to_clockwise_90_rotation_direction(direction):
    if direction == '<':
        return '^'
    elif direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    return direction


def get_ghost_positions(grid, rows, cols):
    ghost_positions = []
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v in ['<', '>', '^', 'v']:
                ghost_positions.append((r, c, v))
    return ghost_positions


def get_ghostless_grid(grid, rows, cols):
    ghostless_grid = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v in ['<', '>', '^', 'v']:
                ghostless_grid[r][c] = '.'
    return ghostless_grid


def get_next_position_moving_in_current_direction(r, c, d):
    next_r, next_c = r, c
    if d == '<':
        next_c -= 1
    elif d == '>':
        next_c += 1
    elif d == '^':
        next_r -= 1
    elif d == 'v':
        next_r += 1  
    return next_r, next_c


def to_reversed_direction(d):
    if d == '<':
        return '>'
    elif d == '>':
        return '<'
    elif d == '^':
        return 'v'
    elif d == 'v':
        return '^'


def plot_new_ghost_positions(ghost_positions, ghostless_grid):
    new_grid = [row[:] for row in ghostless_grid]
    for r, c, d in ghost_positions:
        new_grid[r][c] = d
    return new_grid


def get_ghost_positions_with_ids(grid, rows, cols):
    ghost_positions = []
    id = 0
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v in ['<', '>', '^', 'v']:
                ghost_positions.append((id, r, c, v))
                id += 1
    return ghost_positions