from helpers import logging_helper, file_helper
from dataclasses import dataclass

logger = logging_helper.get_logger_instance()


import common 


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    return common.solve_for_clockhands(text)