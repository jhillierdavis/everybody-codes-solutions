from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

import common

def grid_replace_all_values(grid, old_value, new_value):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == old_value:
                grid[i][j] = new_value
    return grid


def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    sections = text.split("\n\n")

    grid2d_1 = grid_helper.to_grid2d(sections[0])
    grid2d_2 = grid_helper.to_grid2d(sections[1])

    colours = ['C','M','Y','K']
    colour_combinations = [[c1, c2, c3, c4] for c1 in colours for c2 in colours if c1 != c2 for c3 in colours if c3 != c1 and c3 != c2 for c4 in colours if c4 != c1 and c4 != c2 and c4 != c3]
    #logger.debug(f"Colour combinations: {colour_combinations}")

    width = grid2d_1.width
    height = grid2d_1.height
    max_white_crystals = 0
    for colour_group in colour_combinations:
        try_grid = grid_helper.clone(grid2d_2.grid)
        #logger.debug(f"Trying colour set: {colour_group}")
        for i, colour in enumerate(colour_group):
            #logger.debug(f"Trying colour {colour} at position {i}")
            grid_replace_all_values(try_grid, str(i+1), colour)

        combined_grid = common.combine_grids(grid2d_1, grid_helper.Grid2d(try_grid, width, height))

        colour_map = common.to_colour_map(combined_grid, width, height)

        white_crystals = common.calculate_white_crystal_cubes(colour_map)
        if white_crystals > max_white_crystals:
            max_white_crystals = white_crystals
    return max_white_crystals