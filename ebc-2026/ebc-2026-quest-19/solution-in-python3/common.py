from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def combine_grids(grid2d_1, grid2d_2):
    #logger.debug("Combining grids")
    #logger.debug(f"Grid 1: {grid2d_1.width } x {grid2d_1.height}")
    #logger.debug(f"Grid 2: {grid2d_2.width } x {grid2d_2.height}")

    combined_grid = grid_helper.clone(grid2d_1.grid)
    width = grid2d_1.width
    height = grid2d_1.height
    for r in range(height):
        for c in range(width):
            v1 = grid2d_1.grid[r][c] 
            v2 = grid2d_2.grid[r][c] 

            if v1 == 'K' or v2 == 'K':
                combined_grid[r][c] = 'K'
            elif (v1 == 'C' and v2 == 'M') or (v1 == 'M' and v2 == 'C'):
                combined_grid[r][c] = 'B'
            elif (v1 == 'M' and v2 == 'Y') or (v1 == 'Y' and v2 == 'M'):
                combined_grid[r][c] = 'R'
            elif (v1 == 'C' and v2 == 'Y') or (v1 == 'Y' and v2 == 'C'):
                combined_grid[r][c] = 'G'

    return combined_grid


def to_colour_map(combined_grid, width, height):
    colour_map = dict()
    colour_map['K'] = 0
    colour_map['B'] = 0
    colour_map['G'] = 0
    colour_map['C'] = 0
    colour_map['R'] = 0
    colour_map['M'] = 0
    colour_map['Y'] = 0
    for r in range(height):
        for c in range(width):
            #logger.debug(combined_grid[r][c])
            if combined_grid[r][c] in colour_map:
                colour_map[combined_grid[r][c]]    += 1
    return colour_map


def calculate_white_crystal_cubes(colour_map):
    sorted_colours = sorted(colour_map.items(), key=lambda x: x[1], reverse=True)

    result = 1
    for i, (colour, count) in enumerate(sorted_colours):
        #logger.info(f"Rank {i+1}: {colour} with count {count}")
        if i < 3:
            result *= count
    return result