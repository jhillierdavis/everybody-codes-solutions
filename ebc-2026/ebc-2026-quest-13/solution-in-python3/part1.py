from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")
    return -1