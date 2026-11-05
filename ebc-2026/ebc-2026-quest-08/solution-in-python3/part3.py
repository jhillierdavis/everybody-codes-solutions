

from helpers import logging_helper, file_helper, grid_helper   
import common

logger = logging_helper.get_logger_instance()


def get_warrier_count(grid, rows, cols):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '9':
                count += 1
    return count


def get_tree_count(grid, rows, cols):
    tree_count = 0
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value.isdigit():
                tree_count += 1
    return tree_count

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
        if next_value.isdigit():
            next_num = int(next_value)
            if next_num <= num - x:
                #logger.debug(f"Clearing shaded tree cell at ({next_r}, {next_c}) with value {next_value} num={num} x={x}")
                shaded_trees.add((next_r, next_c))
        r, c = next_r, next_c 
    return shaded_trees


def get_unshaded_grid_using_shared_direction(grid, rows, cols, direction_function):

    #for r in range(rows-1, 0, -1):
    shaded_trees = set()
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value.isdigit():
                num = int(value)
                shaded_trees.update(direction_function(grid, rows, cols, r, c, num))

    unshaded_grid = grid_helper.clone(grid)
    for r, c in shaded_trees:
        unshaded_grid[r][c] = '.'
    for r in range(rows):
        for c in range(cols):
            if unshaded_grid[r][c] == 'X':
                unshaded_grid[r][c] = '.'
    return unshaded_grid


def increment_tree_heights(grid, rows, cols):
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value.isdigit():
                new_num = int(value) + 1
                new_value = new_num if new_num < 10 else 'X'
                grid[r][c] = str(new_value)


def merge_grids(grid, next_grid, rows, cols):
    for r in range(rows):
        for c in range(cols):       
            if next_grid[r][c].isdigit():
                grid[r][c] = next_grid[r][c]
            elif next_grid[r][c] == 'X' and grid[r][c] == '9':
                grid[r][c] = 'X'


def grow_existing_warriers(grid, rows, cols):  
    seed_count = 0
    for r in range(rows):
        for c in range(cols):
            value = grid[r][c]
            if value == 'X':
                grid[r][c] = 'Y'
            elif value == 'Y':
                grid[r][c] = 'Z'
            elif value == 'Z':
                grid[r][c] = '1'
                seed_count += 1
    return seed_count

 
def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid, rows, cols = grid_helper.to_grid(text)
    logger.debug(f"Grid:\n{grid_helper.to_string(grid)}")
  
    total_energy_count = 0
    total_warrier_count = 0
    for i in range(1, 100000):

        
        direction = i % 6
        if direction == 1:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_south_east)
        elif direction == 2:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_south_west)
        elif direction == 3:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_west)
        elif direction == 4:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_north_west)
        elif direction == 5:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_north_east)
        elif direction == 0:
            next_grid = get_unshaded_grid_using_shared_direction(grid, rows, cols, get_shaded_trees_to_east)


        energy_count = get_tree_count(next_grid, rows, cols) 
        warrier_count = get_warrier_count(next_grid, rows, cols)
        
        #logger.debug(f"Next grid after round {i}:\n{grid_helper.to_string(next_grid)}")

        increment_tree_heights(next_grid, rows, cols)



        grow_existing_warriers(grid, rows, cols)
        #logger.debug(f"Grid after growing warriers in round {i}:\n{grid_helper.to_string(grid)}")
        merge_grids(grid, next_grid, rows, cols)
        #logger.debug(f"Merged grid after round {i}:\n{grid_helper.to_string(grid)}")

        logger.debug(f"Round {i} direction={direction}: Energy count = {energy_count}, Warrier count = {warrier_count}")

        total_energy_count += energy_count
        total_warrier_count += warrier_count
        if total_warrier_count >= 100000:
            logger.debug(f"Total Warrier count reached {total_warrier_count} at round {i}, stopping")
            break
    logger.debug(f"Total Energy count = {total_energy_count}, Total Warrier count = {total_warrier_count}")
    return total_energy_count