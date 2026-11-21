from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common

def solve_part2(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")
    symbols_map = common.get_symbol_map()
    ans = 0
    for line in text.splitlines():
        total = 0
        if not common.validate_equation_using_base11(line):
            print(f"INVALID : {line}")
        else:
            values = line.split(' ')
            for value in values:
                for char in value:
                    total += symbols_map.get(char, 0)
                print(f"Value: {value}, Total: {total}")
            ans += total

    return common.decimal_to_base11(ans)