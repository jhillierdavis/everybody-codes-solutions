from helpers import logging_helper
from dataclasses import dataclass

logger = logging_helper.get_logger_instance()


from math import gcd
from functools import reduce

def lcm(numbers):
    """
    Return the Lowest Common Multiple (LCM) of a collection
    of positive non-zero integers.

    Args:
        numbers: Iterable of positive non-zero integers.

    Returns:
        Integer LCM of all values.

    Raises:
        ValueError: If the input is empty or contains
                    non-positive integers.
    """
    numbers = list(numbers)

    if not numbers:
        raise ValueError("Input must contain at least one integer")

    if any(n <= 0 for n in numbers):
        raise ValueError("All integers must be positive and non-zero")

    def lcm_pair(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm_pair, numbers)


@dataclass(frozen=True)
class Clockhand:
    id: int
    increment: int
    is_clockwise: bool
    start: int
    steps: int


def solve_for_clockhands(text):
    input_map = {}
    for i, line in enumerate(text.splitlines()):
        if i == 0:
            parts = (line.removeprefix("hands ")).split(":")
            input_map[i] = [int(p) for p in parts]
        elif i == 1:
            parts = (line.removeprefix("direction ")).split(":")
            input_map[i] = [True if p == "CW" else False for p in parts]
        elif i == 2:
            parts = (line.removeprefix("current ")).split(":")
            input_map[i] = [int(p) for p in parts]
        elif i == 3:
            parts = (line.removeprefix("move ")).split(":")
            input_map[i] = [int(p) for p in parts]
        logger.debug(f"input_map{i}: {input_map[i]}")

    
    clockhands = []
    for i, parts in enumerate(input_map[0]):
        clockhand = Clockhand(
            id=i+1,
            increment=input_map[0][i],
            is_clockwise=input_map[1][i],
            start=input_map[2][i],
            steps=input_map[3][i]
        )
        clockhands.append(clockhand)

    logger.debug(f"Clockhands: {clockhands}")

    lcm_value = lcm([ch.increment for ch in clockhands])
    logger.debug(f"LCM value: {lcm_value}")


    for c in clockhands:
        #logger.debug(f"Clockhand {c.id}: start={c.start}, steps={c.steps}, increment={c.increment}, is_clockwise={c.is_clockwise}")   

        interval = lcm_value // c.increment
        #logger.debug(f"Clockhand {c.id}: interval={interval}")

        start_interval = c.start * interval
        #logger.debug(f"Clockhand {c.id}: start_interval={start_interval}")


    max_steps = max(c.steps for c in clockhands)
    logger.debug(f"Max steps: {max_steps}")

    position_map = {}
    for c in clockhands:
        interval = lcm_value // c.increment
        current_position = c.start * interval
        position_map[c.id] = [current_position]

    #logger.debug(f"Position map: {position_map}")

    
    for t in range(max_steps):
        for c in clockhands:
            current_position = position_map[c.id][-1] # Last known position
            if t < c.steps:
                interval = lcm_value // c.increment
                if c.is_clockwise:
                    current_position += interval
                else:
                    current_position -= interval
                current_position = current_position % lcm_value
                #logger.debug(f"Clockhand {c.id}: current_position={current_position} at time={t}")
            position_map[c.id].append(current_position)

    #logger.debug(f"Final position map: {position_map}")
    return count_hand_crossings(position_map, lcm_value)


from itertools import combinations


def count_hand_crossings(hand_positions, clock_size=12):
    if not hand_positions:
        return 0

    n = len(next(iter(hand_positions.values())))

    if any(len(v) != n for v in hand_positions.values()):
        raise ValueError("All hands must have the same number of steps")

    def signed_move(start, end):
        """
        Shortest-path movement around the clock.
        """
        cw = (end - start) % clock_size
        ccw = (start - end) % clock_size

        if cw <= ccw:
            return cw
        return -ccw

    crossings = 0

    for h1, h2 in combinations(hand_positions, 2):
        a = hand_positions[h1]
        b = hand_positions[h2]

        for i in range(n - 1):

            # Meeting at the end of the interval.
            if a[i + 1] == b[i + 1]:
                crossings += 1
                continue

            a0 = a[i]
            b0 = b[i]

            da = signed_move(a[i], a[i + 1])
            db = signed_move(b[i], b[i + 1])

            rel_start = a0 - b0
            rel_end = (a0 + da) - (b0 + db)

            if rel_start == 0:
                continue

            if rel_start * rel_end < 0:
                crossings += 1

    return crossings