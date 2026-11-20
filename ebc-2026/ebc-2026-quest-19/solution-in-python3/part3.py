from itertools import count
import re

from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

import common

def calculate_max_crystals(colour_map):
    reallocation_count = 0
    for k,v in colour_map.items():
        if k in ['C','M','Y']:
            reallocation_count += v
    #logger.debug(f"Reallocation count: {reallocation_count}")

    colour_sub_map = {k: v for k, v in colour_map.items() if k not in ['C','M','Y']}

    div = reallocation_count // 3
    remainder = reallocation_count % 3

    skip_list = ['K']
    k_value = colour_sub_map.get('K', 0)
    if k_value >= div:
        div = reallocation_count // 2
        remainder = reallocation_count % 2
        min_value = div
        min_key = None
        for k, v in colour_sub_map.items():
            if k not in skip_list and v < k_value:
                if v < min_value:
                    min_value = v
                    min_key = k
        skip_list.append(min_key)

    for k in colour_sub_map.keys():
        if k not in skip_list:
            colour_sub_map[k] += div

    for k in colour_sub_map.keys():
        if k not in skip_list and remainder > 0:
            colour_sub_map[k] += 1
            remainder -= 1

    sorted_colour_sub_map = dict(sorted(colour_sub_map.items(), key=lambda item: item[1], reverse=True))
    #logger.debug(f"Sorted colour sub map: {sorted_colour_sub_map}")

    crystals = common.calculate_white_crystal_cubes( colour_sub_map )
    #logger.debug(f"Crystals: {crystals}")
    return crystals


def solve_part3(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)  

    colour_map = common.to_colour_map(grid2d.grid, grid2d.width, grid2d.height)  
    logger.debug(f"Colour map: {colour_map}")

    """
    total = grid2d.width * grid2d.height
    div = total // 3
    remainder = total % 3
    value = (total - remainder) // div
    logger.debug(f"Total: {total} Div: {div} Remainder: {remainder} value: {value}")
    ans  = 1
    if div >= 3:
        ans = value * value * value
    elif div == 2:
        ans = value * value * remainder
    """
    ans = calculate_max_crystals(colour_map)
    return ans