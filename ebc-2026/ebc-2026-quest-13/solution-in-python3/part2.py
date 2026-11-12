from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common


def solve_for_clockhands(filename):
    text = file_helper.get_text(filename) 
    return common.solve_for_clockhands(text)


def solve_part2(filename):
    sections = file_helper.get_text_sections(filename)
    logger.debug(f"Sections: {sections}")

    ans = 0
    
    for i, s in enumerate(sections):
        logger.debug(f"Processing section {i}: {s}")
        result = common.solve_for_clockhands(s)
        logger.debug(f"Result for section {i}: {result}")
        ans += result
    
    return ans