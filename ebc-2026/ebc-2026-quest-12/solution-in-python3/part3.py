from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


def solve_part3(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)
    return grid_helper.minimum_segment_cover(grid2d.grid)
