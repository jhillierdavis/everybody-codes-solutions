# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def count_potions_per_creature(creature_label):
    if 'B' == creature_label: # Badass Beetle (B)
        return 1
    elif 'C' == creature_label: # Creepy Cockroach (C):
        return 3
    elif 'D' == creature_label: # 'Diabolical Dragonfly' - added in Part 2
            return 5
    
    # Others, e.g.: Ancient Ant (A), ignored as no potion required 
    return 0


def solve_part1(input):
    ans = 0
    for ch in input:
        ans += count_potions_per_creature(ch)
    return ans


def solve_part2(input):
    ans = 0
    last_ch = None
    for idx, ch in enumerate(input):
        if idx % 2 == 0:
            last_ch = ch
        else:
            last_potions = count_potions_per_creature(last_ch)
            current_potions = count_potions_per_creature(ch)

            logger.debug(f"last_ch={last_ch} current_ch={ch} last_potions={last_potions} current_potents={current_potions}")
            
            ans += last_potions
            ans += current_potions
            if not (last_ch == 'x' or ch == 'x'):                
                ans += 2
            
    return ans


def get_grouped_substrings(str, size):
    x = size
    groups = [str[y-x:y] for y in range(x, len(str)+x,x)]
    return groups


def solve_part3(input):
    group_chars = get_grouped_substrings(input, 3)

    ans = 0
    for gc in group_chars:

        x_count = gc.count('x')
        if x_count == 0: # Add extra 2 per creature (as set of 3)
            ans += 6
        elif x_count == 1: # Add extra 1 per creature (as set of 2)
            ans += 2

        for w in gc:
            ans += count_potions_per_creature(w)
    return ans