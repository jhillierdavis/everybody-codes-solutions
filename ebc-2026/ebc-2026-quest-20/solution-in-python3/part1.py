from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import re

def validate_equation(line):
    """
    Returns True if the arithmetic equation is mathematically valid,
    otherwise False.
    """
    if '=' not in line:
        return False

    left, right = line.split('=', 1)

    try:
        return eval(left.strip()) == eval(right.strip())
    except Exception:
        return False


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    symbols_map = dict()
    symbols_map['0'] = 6
    symbols_map['1'] = 2
    symbols_map['2'] = 5
    symbols_map['3'] = 5
    symbols_map['4'] = 4
    symbols_map['5'] = 5
    symbols_map['6'] = 6
    symbols_map['7'] = 3
    symbols_map['8'] = 7
    symbols_map['9'] = 6
    symbols_map['+'] = 2
    symbols_map['-'] = 1
    symbols_map['='] = 2


    ans = 0
    for line in text.splitlines():
        total = 0
        if not validate_equation(line):
            print(f"INVALID : {line}")
        else:
            values = line.split(' ')
            for value in values:
                for char in value:
                    total += symbols_map.get(char, 0)
                print(f"Value: {value}, Total: {total}")
            ans += total

    return ans