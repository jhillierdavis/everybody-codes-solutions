from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

import common

def solve_part2(filename, max_collisions):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols  = grid_helper.to_grid(text)

    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    
    ghost_positions = common.get_ghost_positions_with_ids(grid, rows, cols)
    wall_positions = common.get_wall_positions(grid, rows, cols)

    logger.debug(f"Ghost Positions: {ghost_positions}")
    logger.debug(f"Wall Positions: {wall_positions}")

    #ghostless_grid = common.get_ghostless_grid(grid, rows, cols)

    id_to_collision_map = {}
    for id, r, c, d in ghost_positions:
        id_to_collision_map[id] = max_collisions

    total_collistion_count = 0
    for i in range(1000000):
        new_ghost_positions = []
        wall_collision_count = 0
        ghost_collision_count = 0
        collistion_count = 0
        for id, r, c, d in ghost_positions:
            next_r, next_c = common.get_next_position_moving_in_current_direction(r, c, d)
            if (next_r, next_c) in wall_positions:
                wall_collision_count += 1
                if id_to_collision_map[id] >= 1:
                        id_to_collision_map[id] -= 1
                if id_to_collision_map[id] > 0:
                    new_ghost_positions.append((id, r, c, common.to_clockwise_90_rotation_direction(d)))
            else:
                new_ghost_positions.append((id, next_r, next_c, d))
        

        new_colliding_ghost_positions = []
        collision_position_to_direction_map = {}

        for id, r, c, d in new_ghost_positions:
            pos = (r, c)
            if pos in collision_position_to_direction_map:
                collision_position_to_direction_map[pos].append((id, d))
            else:
                collision_position_to_direction_map[pos] = [(id, d)]

        for pos, id_d_pairs in collision_position_to_direction_map.items():
            if len(id_d_pairs) > 1:
                ghost_collision_count += len(id_d_pairs)
                for id, d in id_d_pairs:
                    if id_to_collision_map[id] >= 1:
                        id_to_collision_map[id] -= 1
                    if id_to_collision_map[id] > 0:
                            new_colliding_ghost_positions.append((id, pos[0], pos[1], common.to_reversed_direction(d)))                
            else:
                id, d = id_d_pairs[0]
                new_colliding_ghost_positions.append((id, pos[0], pos[1], d))
        ghost_positions = new_colliding_ghost_positions

        ghost_count = 0
        for _, v in id_to_collision_map.items():
            if v > 0:
                ghost_count += 1
        logger.debug(f"Round {i+1} : ghost count: {ghost_count} id_to_collision_map: {id_to_collision_map}")
        if ghost_count <= 0:
            break
        
        collistion_count = wall_collision_count + ghost_collision_count
        total_collistion_count += collistion_count
        logger.debug(f"Round {i+1} : collisions: {collistion_count}, wall collisions: {wall_collision_count}, ghost collisions: {ghost_collision_count}")

        
        #new_grid = common.plot_new_ghost_positions(ghost_positions, ghostless_grid)
        #logger.debug(f"New Grid after Round {i+1}:\n{grid_helper.to_string(new_grid)}")

    return i + 1