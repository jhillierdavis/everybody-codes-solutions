from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common

def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")
    symbols_map = common.get_symbol_map()
    ans = 0
    for line in text.splitlines():
        is_valid =  common.validate_equation_using_base11(line)
        if not is_valid: 
            logger.debug(f"INVALID : {line}")
            variants = common.get_single_change_expression_variants(line)
            for variant in variants:
                is_valid = common.validate_equation_using_base11(variant)
                if is_valid:
                    logger.debug(f"VALID VARIANT: {variant}")
                    line = variant
                    break
            

        if is_valid:
            total = 0
            values = line.split(' ')
            for value in values:
                for char in value:
                    total += symbols_map.get(char, 0)
                #logger.debug(f"Value: {value}, Total: {total}")
            ans += total

    return common.decimal_to_base11(ans)