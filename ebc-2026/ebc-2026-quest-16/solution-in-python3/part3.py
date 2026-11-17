from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

#import common


def solve_part3(filename, size):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    return -1