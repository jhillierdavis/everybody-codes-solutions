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


def solve_part1(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols  = grid_helper.to_grid(text)

    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    
    ghost_positions = get_ghost_positions(grid, rows, cols)
    wall_positions = get_wall_positions(grid, rows, cols)

    logger.debug(f"Ghost Positions: {ghost_positions}")
    logger.debug(f"Wall Positions: {wall_positions}")

    ghostless_grid = get_ghostless_grid(grid, rows, cols)


    total_collistion_count = 0
    for i in range(10):
        new_ghost_positions = []
        wall_collision_count = 0
        ghost_collision_count = 0
        collistion_count = 0
        for r, c, d in ghost_positions:
            next_r, next_c = get_next_position_moving_in_current_direction(r, c, d)
            if (next_r, next_c) in wall_positions:
                wall_collision_count += 1
                new_ghost_positions.append((r, c, to_clockwise_90_rotation_direction(d)))
            else:
                new_ghost_positions.append((next_r, next_c, d))
        

        new_colliding_ghost_positions = []
        collision_position_to_direction_map = {}

        for r, c, d in new_ghost_positions:
            pos = (r, c)
            if pos in collision_position_to_direction_map:
                collision_position_to_direction_map[pos].append(d)
            else:
                collision_position_to_direction_map[pos] = [d]

        for pos, directions in collision_position_to_direction_map.items():
            if len(directions) > 1:
                ghost_collision_count += len(directions)
                for d in directions:
                    new_colliding_ghost_positions.append((pos[0], pos[1], to_reversed_direction(d)))
            else:
                new_colliding_ghost_positions.append((pos[0], pos[1], directions[0]))
        ghost_positions = new_colliding_ghost_positions
        
        collistion_count = wall_collision_count + ghost_collision_count
        total_collistion_count += collistion_count
        logger.debug(f"Round {i+1} : collisions: {collistion_count}, wall collisions: {wall_collision_count}, ghost collisions: {ghost_collision_count}")
        
        new_grid = plot_new_ghost_positions(ghost_positions, ghostless_grid)
        #logger.debug(f"New Grid after Round {i+1}:\n{grid_helper.to_string(new_grid)}")

    return total_collistion_count