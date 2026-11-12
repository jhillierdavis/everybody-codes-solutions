from helpers import logging_helper, number_helper
from dataclasses import dataclass

logger = logging_helper.get_logger_instance()

import crossings

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

    lcm_value = number_helper.lcm([ch.increment for ch in clockhands])
    logger.debug(f"LCM value: {lcm_value}")


    for c in clockhands:
        #logger.debug(f"Clockhand {c.id}: start={c.start}, steps={c.steps}, increment={c.increment}, is_clockwise={c.is_clockwise}")   

        interval = lcm_value // c.increment
        #logger.debug(f"Clockhand {c.id}: interval={interval}")

        start_interval = c.start * interval
        #logger.debug(f"Clockhand {c.id}: start_interval={start_interval}")


    max_steps = max(c.steps for c in clockhands)
    logger.debug(f"Max steps: {max_steps}")

    # Set initial positions for each clockhand
    position_map = {}
    for c in clockhands:
        interval = lcm_value // c.increment
        current_position = c.start * interval
        key = (c.id, c.increment if c.is_clockwise else -c.increment)
        position_map[key] = [current_position]

    logger.debug(f"Initial position map for clockhands: {position_map}")

    
    for t in range(max_steps):
        for c in clockhands:
            key = (c.id, c.increment if c.is_clockwise else -c.increment)
            current_position = position_map[key][-1] # Last known position
            if t < c.steps:
                interval = lcm_value // c.increment
                if c.is_clockwise:
                    current_position += interval
                else:
                    current_position -= interval
                current_position = current_position % lcm_value
                #logger.debug(f"Clockhand {c.id}: current_position={current_position} at time={t}")
            position_map[key].append(current_position)

    logger.debug(f"Final position map for clockhands: \n{position_map}")
    return crossings.count_hand_crossings(position_map, lcm_value)


