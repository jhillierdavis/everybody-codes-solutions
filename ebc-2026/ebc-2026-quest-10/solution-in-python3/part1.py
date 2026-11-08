from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

import common


def solve_part1(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols  = grid_helper.to_grid(text)

    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    
    ghost_positions = common.get_ghost_positions(grid, rows, cols)
    wall_positions = common.get_wall_positions(grid, rows, cols)

    logger.debug(f"Ghost Positions: {ghost_positions}")
    logger.debug(f"Wall Positions: {wall_positions}")

    ghostless_grid = common.get_ghostless_grid(grid, rows, cols)


    total_collistion_count = 0
    for i in range(10):
        new_ghost_positions = []
        wall_collision_count = 0
        ghost_collision_count = 0
        collistion_count = 0
        for r, c, d in ghost_positions:
            next_r, next_c = common.get_next_position_moving_in_current_direction(r, c, d)
            if (next_r, next_c) in wall_positions:
                wall_collision_count += 1
                new_ghost_positions.append((r, c, common.to_clockwise_90_rotation_direction(d)))
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
                    new_colliding_ghost_positions.append((pos[0], pos[1], common.to_reversed_direction(d)))
            else:
                new_colliding_ghost_positions.append((pos[0], pos[1], directions[0]))
        ghost_positions = new_colliding_ghost_positions
        
        collistion_count = wall_collision_count + ghost_collision_count
        total_collistion_count += collistion_count
        logger.debug(f"Round {i+1} : collisions: {collistion_count}, wall collisions: {wall_collision_count}, ghost collisions: {ghost_collision_count}")
        
        #new_grid = common.plot_new_ghost_positions(ghost_positions, ghostless_grid)
        #logger.debug(f"New Grid after Round {i+1}:\n{grid_helper.to_string(new_grid)}")

    return total_collistion_count