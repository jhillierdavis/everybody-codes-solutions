from helpers import logging_helper

logger = logging_helper.get_logger_instance()

def get_symbol_map():
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
    symbols_map['A'] = 6
    return symbols_map


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


def base11_expressions_to_decimal(expr):
    """
    Converts a base-11 arithmetic expression to its decimal equivalent.
    """
    values = expr.split(' ')
    left_value = base11_to_decimal(values[0])
    right_value = base11_to_decimal(values[2])

    if values[1] == '+':
        return left_value + right_value
    elif values[1] == '-':
        return left_value - right_value
    else:
        raise ValueError(f"Unsupported operator: {values[1]}")


def validate_equation_using_base11(line):
    """
    Returns True if the arithmetic equation is mathematically valid,
    otherwise False.
    """
    if '=' not in line:
        return False

    left, right = line.split('=', 1)
    logger.debug(f"Left: {left}, Right: {right}")
  
    return base11_expressions_to_decimal(left.strip()) == base11_expressions_to_decimal(right.strip())


def base11_to_decimal(s):
    result = 0
    for i, char in enumerate(reversed(s)):
        if char == 'A':
            value = 10
        else:
            value = int(char)
        result += value * (11 ** i)
    return result


def decimal_to_base11(n):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        remainder = n % 11
        if remainder == 10:
            digits.append('A')
        else:
            digits.append(str(remainder))
        n //= 11
    return int(''.join(reversed(digits)))