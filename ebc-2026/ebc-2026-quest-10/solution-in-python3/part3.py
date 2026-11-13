
from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

import common

"""
TODO: Change cycle match to:
* Eclude ID (doesn't matter)
* Exclude ID (doesn't matter) - Only consider positions and directions for cycle detection
* Use number of collisions in tuple (r, c, d, collisions) & time as value in cycle detection map
* Change d to an integer representing direction
* When a cycle is detected either advance by old t - new t (if no ghosts disappear) or to just  (1 round) before the next ghost disappears 
"""

def get_ghost_positions_with_ids_and_zero_collisions(grid, rows, cols):
    ghost_positions = []
    id = 0
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v in ['<', '>', '^', 'v']:
                # Append initial ghost with id, row position, column position, direction, and zero collisions
                ghost_positions.append((id, r, c, v, 0)) 
                id += 1
    return ghost_positions


def initialise_id_to_collision_map(ghost_positions, value):
    id_to_collision_map = {}
    for id, r, c, d, h  in ghost_positions:
        id_to_collision_map[id] = value
    return id_to_collision_map


def copy_map_where_value_above_zero(map):
    new_map = {}
    for k, v in map.items():
        if v > 0:
            new_map[k] = v
    return new_map


def deduct_cycle_collisions(id_to_collision_map, seen_id_to_collision_map):
    count = 0
    new_id_to_collision_map = copy_map_where_value_above_zero(id_to_collision_map)

    is_above_zero = True
    last_id_to_collision_map = new_id_to_collision_map.copy()
    while is_above_zero:
        
        for id, seen_collisions_for_id in seen_id_to_collision_map.items():
            new_value = new_id_to_collision_map[id] - seen_collisions_for_id
            if new_value > 0:
                new_id_to_collision_map[id] = new_value
            else:
                is_above_zero = False
                break
        if is_above_zero:
            count += 1
            last_id_to_collision_map = new_id_to_collision_map.copy()
    return count, last_id_to_collision_map


def legacy_solve_part3(filename, max_collisions):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols  = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    
    ghost_positions = get_ghost_positions_with_ids_and_zero_collisions(grid, rows, cols)
    wall_positions = common.get_wall_positions(grid, rows, cols)

    #logger.debug(f"Ghost Positions: {ghost_positions}")
    #logger.debug(f"Wall Positions: {wall_positions}")

    #ghostless_grid = common.get_ghostless_grid(grid, rows, cols)

    id_to_collision_map = initialise_id_to_collision_map(ghost_positions, max_collisions)

    seen_round_positions = {} # Map of positions to round number
    #seen_collisions = 0
    #seen_id_to_collision_map = initialise_id_to_collision_map(ghost_positions, 0)
    total_collistion_count = 0
    i = 0 # Round count tracker
    while True:
        i += 1
        new_ghost_positions = []
        wall_collision_count = 0
        ghost_collision_count = 0
        collistion_count = 0
        for id, r, c, d, h in ghost_positions:
            next_r, next_c = common.get_next_position_moving_in_current_direction(r, c, d)
            if (next_r, next_c) in wall_positions: # Wall collision 
                #wall_collision_count += 1
                if h < max_collisions:
                    h += 1
                
                if id_to_collision_map[id] > 0: # Ghost still present
                    new_ghost_positions.append((id, r, c, common.to_clockwise_90_rotation_direction(d), h))
                #else:
                    #seen_round_positions = {} # Reset seen positions when a ghost is removed due to no remaining collisions
                    #seen_id_to_collision_map = initialise_id_to_collision_map(ghost_positions, 0) # Reset seen id_to_collision_map as well

            else: # No wall collision, move ghost to next position
                new_ghost_positions.append((id, next_r, next_c, d, h))
        

        new_colliding_ghost_positions = []
        collision_position_to_direction_map = {}

        # Build a map of collision positions to the directions of ghosts at those positions
        for id, r, c, d, h in new_ghost_positions:
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
                        seen_collisions += 1
                        seen_id_to_collision_map[id] += 1
                    if id_to_collision_map[id] > 0:
                        new_colliding_ghost_positions.append((id, pos[0], pos[1], common.to_reversed_direction(d), h))
                    else:
                        seen_round_positions = {} # Reset seen positions when a ghost is removed due to no remaining collisions
                        seen_id_to_collision_map = initialise_id_to_collision_map(ghost_positions, 0) # Reset seen id_to_collision_map as well
                        seen_collisions += 1
            else:
                id, d = id_d_pairs[0]
                new_colliding_ghost_positions.append((id, pos[0], pos[1], d, h))
        ghost_positions = new_colliding_ghost_positions

        # Check the number of remaining ghosts
        ghost_count = 0
        for _, v in id_to_collision_map.items():
            if v > 0:
                ghost_count += 1
        #logger.debug(f"Round {i+1} : ghost count: {ghost_count} id_to_collision_map: {id_to_collision_map}")
        if ghost_count <= 0:
            break
        
        collistion_count = wall_collision_count + ghost_collision_count
        total_collistion_count += collistion_count
        #logger.debug(f"Round {i+1} : collisions: {collistion_count}, wall collisions: {wall_collision_count}, ghost collisions: {ghost_collision_count}")

        
        #new_grid = common.plot_new_ghost_positions(ghost_positions, ghostless_grid)
        #logger.debug(f"New Grid after Round {i+1}:\n{grid_helper.to_string(new_grid)}")


        # Check for repeat cycles
        round_positions = tuple( (r, c, d) for id, r, c, d, h in ghost_positions)
        if round_positions in seen_round_positions:
            id_to_collision_map = copy_map_where_value_above_zero(id_to_collision_map)
            #logger.debug(f"Updated id_to_collision_map: {id_to_collision_map}")
            cycle_size = len(seen_round_positions)
            logger.debug(f"Repeat cycle detected at round {i+1} cycle of size {cycle_size} with positions: {round_positions}, seen_round_positions[round_positions]: {seen_round_positions[round_positions]}")
            count, id_to_collision_map = deduct_cycle_collisions(
                id_to_collision_map, seen_id_to_collision_map
            )
            i += count
            seen_round_positions = {} # Reset seen positions after deducting cycle collisions
        
        seen_id_to_collision_map = copy_map_where_value_above_zero(id_to_collision_map)
        seen_round_positions[round_positions] = seen_id_to_collision_map.copy()

    logger.debug(f"i={i}")
    #return i
    return 0


def get_ghost_count(ghost_positions, max_collisions):
    return len([1 for id, r, c, d, h in ghost_positions if h < max_collisions])

def solve_part3(filename, max_collisions):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols  = grid_helper.to_grid(text)

    #logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
    
    ghost_positions = get_ghost_positions_with_ids_and_zero_collisions(grid, rows, cols)
    wall_positions = common.get_wall_positions(grid, rows, cols)

    ghost_count = get_ghost_count(ghost_positions, max_collisions)
    round_number = 0
    while ghost_count > 0:
        new_ghost_positions = []   

        for id, r, c, d, h in ghost_positions:
            next_r, next_c = common.get_next_position_moving_in_current_direction(r, c, d)
            if (next_r, next_c) in wall_positions: # Wall collision 
                #wall_collision_count += 1
                if h < max_collisions:
                    h += 1
                
                if id_to_collision_map[id] > 0: # Ghost still present
                    new_ghost_positions.append((id, r, c, common.to_clockwise_90_rotation_direction(d), h))
                #else:
                    #seen_round_positions = {} # Reset seen positions when a ghost is removed due to no remaining collisions
                    #seen_id_to_collision_map = initialise_id_to_collision_map(ghost_positions, 0) # Reset seen id_to_collision_map as well

            else: # No wall collision, move ghost to next position
                new_ghost_positions.append((id, next_r, next_c, d, h))
        
        ghost_positions = new_ghost_positions
        ghost_count = get_ghost_count(ghost_positions, max_collisions)
        round_number += 1
        logger.debug(f"After round {round_number}, ghost count: {ghost_count}")
    return ghost_count