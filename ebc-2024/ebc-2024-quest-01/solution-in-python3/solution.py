# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def solve_part1(input):
    result = 0
    for ch in input:
        if 'B' == ch:
            result += 1
        elif 'C' == ch:
            result += 3
    return result

def count_potions(creature):
    if 'B' == creature:
        return 1
    elif 'C' == creature:
        return 3
    elif 'D' == creature:
            return 5
    return 0


def solve_part2(input):
    ans = 0
    last_ch = None
    for idx, ch in enumerate(input):
        if idx % 2 == 0:
            last_ch = ch
        else:
            last_potions = count_potions(last_ch)
            current_potions = count_potions(ch)

            logger.debug(f"last_ch={last_ch} current_ch={ch} last_potions={last_potions} current_potents={current_potions}")
            
            ans += last_potions
            ans += current_potions
            if not (last_ch == 'x' or ch == 'x'):                
                ans += 2
            
    return ans

def solve_part3(input):
    x=3 
    group_chars = [input[y-x:y] for y in range(x, len(input)+x,x)]

    ans = 0
    for gc in group_chars:

        x_count = gc.count('x')
        if x_count == 0:
            ans += 6
        elif x_count == 1:
            ans += 2

        for w in gc:
            ans += count_potions(w)
    return ans