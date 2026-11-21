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
    #logger.debug(f"Left: {left}, Right: {right}")
  
    return base11_expressions_to_decimal(left.strip()) == base11_expressions_to_decimal(right.strip())


def get_single_change_expression_variants_for_char(expression:str, target:str, replacement:str) -> list[str]:
    variants = set()

    if target in expression:
        index = expression.find(target)
        while index != -1:
            variant = expression[:index] + replacement + expression[index+1:]
            variants.add(variant)
            index = expression.find(target, index + 1)

    return variants


def get_addition_map():
    addition_map = {    
        '0': ['8'],
        '1': ['7'],
        '3': ['9'],
        '5': ['6','9'],
        '6': ['8'],
        '9': ['8'],
        '-': ['+'],
        'A': ['8']
    }
    return addition_map

def get_reduction_map():
    reduction_map = {    
        #'0': ['6','9'],
        '6': ['5'],    
        '7': ['1'],
        '8': ['0','6','9','A'],
        '9': ['3','5'],
        '+': ['-'],
       # 'A': ['9']
    }
    return reduction_map

def get_single_change_expression_variants(expression:str) -> list[str]:
    """
    Generates all possible single-character change variants of the given expression.
    """
    variants = set()

    # Handle direct single-character replacements
    for target, replacement in [('0', '9'), ('2', '3'), ('3', '2'), ('3', '5'), ('5', '3'), ('9', '0')]:
        variants.update(get_single_change_expression_variants_for_char(expression, target, replacement))

    addition_map = get_addition_map()

    # Handle + variants
    """
    if '+' in expression:
        plus_expressions = get_single_change_expression_variants_for_char(expression, '+', '-')

        for k, v_list in addition_map.items():
            for v in v_list:
                for pe in plus_expressions:
                    variants.update(get_single_change_expression_variants_for_char(pe, k, v))
    """
    reduction_map = get_reduction_map()
    

    for ak, av_list in addition_map.items():
        for av in av_list:
            addition_expressions = get_single_change_expression_variants_for_char(expression, ak, av)
            for ae in addition_expressions:
                for k, v_list in reduction_map.items():
                    for v in v_list:
                        variants.update(get_single_change_expression_variants_for_char(ae, k, v))

    # Handle - variants
    for rk, rv_list in reduction_map.items():       
        for rv in rv_list:
            minus_expressions = get_single_change_expression_variants_for_char(expression, rk, rv)
            for me in minus_expressions:
                for k, v_list in addition_map.items():
                    for v in v_list:
                        variants.update(get_single_change_expression_variants_for_char(me, k, v))

    #logger.debug(f"Generated variants for expression '{expression}': {variants}")
    return variants


def base11_to_decimal(s):
    result = 0
    for i, char in enumerate(reversed(s)):
        if char == 'A':
            value = 10
        else:
            value = int(char)
        result += value * (11 ** i)
    return result


def decimal_to_base11(n:int) -> int:
    if n == 0:
        return 0
    
    digits = []
    while n > 0:
        remainder = n % 11
        if remainder == 10:
            digits.append('A')
        else:
            digits.append(str(remainder))
        n //= 11
    return int(''.join(reversed(digits)))