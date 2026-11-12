from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


import common


def solve_for_clockhands(text):
    return common.solve_for_clockhands(text)

def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")
    return -1