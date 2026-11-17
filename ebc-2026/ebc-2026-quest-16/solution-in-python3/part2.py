from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common

def solve_part2(filename, size):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    flip_counts, letters_reversed, transformed = common.count_flips(text * size)    
    return letters_reversed