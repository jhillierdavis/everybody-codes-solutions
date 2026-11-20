from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def combine_grids(grid2d_1, grid2d_2):
    logger.debug("Combining grids")
    logger.debug(f"Grid 1: {grid2d_1.width } x {grid2d_1.height}")
    logger.debug(f"Grid 2: {grid2d_2.width } x {grid2d_2.height}")
    for r in range(grid2d_1.height):
        for c in range(grid2d_1.width):
            v1 = grid2d_1.grid[r][c] 
            v2 = grid2d_2.grid[r][c] 

            if v1 == 'K' or v2 == 'K':
                grid2d_1.grid[r][c] = 'K'
            elif (v1 == 'C' and v2 == 'M') or (v1 == 'M' and v2 == 'C'):
                grid2d_1.grid[r][c] = 'B'
            elif (v1 == 'M' and v2 == 'Y') or (v1 == 'Y' and v2 == 'M'):
                grid2d_1.grid[r][c] = 'R'
            elif (v1 == 'C' and v2 == 'Y') or (v1 == 'Y' and v2 == 'C'):
                grid2d_1.grid[r][c] = 'G'

    return grid2d_1

def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    sections = text.split("\n\n")

    grid2d_1 = grid_helper.to_grid2d(sections[0])
    grid2d_2 = grid_helper.to_grid2d(sections[1])
    
    combined_grid = combine_grids(grid2d_1, grid2d_2)

    colour_map = dict()
    colour_map['K'] = 0
    colour_map['B'] = 0
    colour_map['G'] = 0
    colour_map['C'] = 0
    colour_map['R'] = 0
    colour_map['M'] = 0
    colour_map['Y'] = 0
    for row in range(combined_grid.height):
        for c in range(combined_grid.width):
            logger.debug(combined_grid.grid[row][c])
            if combined_grid.grid[row][c] in colour_map:
                colour_map[combined_grid.grid[row][c]] += 1
    logger.debug(f"Colour map: {colour_map}")
    for colour, count in colour_map.items():
        logger.info(f"{colour}: {count}")

    sorted_colours = sorted(colour_map.items(), key=lambda x: x[1], reverse=True)

    result = 1
    for i, (colour, count) in enumerate(sorted_colours):
        logger.info(f"Rank {i+1}: {colour} with count {count}")
        if i < 3:
            result *= count
    return result