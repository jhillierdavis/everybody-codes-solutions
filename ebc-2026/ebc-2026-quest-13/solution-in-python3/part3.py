from helpers import logging_helper, file_helper, number_helper

logger = logging_helper.get_logger_instance()


import common, crossings

def get_next_signatiure_positions(clockhands, last_positions, lcm_value):
    next_positions = []
    for i, c in enumerate(clockhands):
        current_position = last_positions[i]
        interval = lcm_value // c.increment
        if c.is_clockwise:
            current_position += interval
        else:
            current_position -= interval
        current_position = current_position % lcm_value
        next_positions.append(current_position)
    return next_positions


def get_start_position_map(clockhands, lcm_value):
    position_map = {}
    for c in clockhands:
        interval = lcm_value // c.increment
        current_position = c.start * interval
        key = (c.id, c.increment if c.is_clockwise else -c.increment)
        position_map[key] = [current_position]
    return position_map


def get_next_position_map(clockhands, current_position_map, lcm_value):
    position_map = {}
    for c in clockhands:
        interval = lcm_value // c.increment
        current_position = current_position_map[(c.id, c.increment if c.is_clockwise else -c.increment)][-1] * interval
        key = (c.id, c.increment if c.is_clockwise else -c.increment)
        position_map[key] = [current_position]
    return position_map


def get_clockhand_next_position(clockhand, current_position, lcm_value):
    interval = lcm_value // clockhand.increment
    if clockhand.is_clockwise:
        current_position += interval
    else:
        current_position -= interval
    current_position = current_position % lcm_value
    return current_position


def solve_for_clockhands(text):
    clockhands = common.get_clockhands(text)


    lcm_value = number_helper.lcm([ch.increment for ch in clockhands])
    logger.debug(f"LCM value: {lcm_value}")

    min_steps = min(c.steps for c in clockhands)
    logger.debug(f"Min steps: {min_steps}")
    max_steps = max(c.steps for c in clockhands)
    logger.debug(f"Max steps: {max_steps}")

    # Set initial positions for each clockhand
    last_positions = [c.start * (lcm_value // c.increment) for c in clockhands]

    # Determine cycles
    seen_signatures = []
    for t in range(min_steps):
        signatures = get_next_signatiure_positions(clockhands, last_positions, lcm_value)
        signature = tuple(signatures)
        if signature in seen_signatures:
            fast_forward_steps = min_steps // t
            logger.debug(f"Repeated signature found: {signature} at time {t}")
            logger.debug(f"Fast forward steps: {fast_forward_steps}")
            break
        seen_signatures.append(signature)
        last_positions = signatures
 

    position_map = get_start_position_map(clockhands, lcm_value)
    logger.debug(f"Start position map for clockhands: {position_map}")


    crossing_pairs_of_clockhands_count = 0
    for t in range(max_steps):
        for c in clockhands:
            key = (c.id, c.increment if c.is_clockwise else -c.increment)
            current_position = position_map[key][-1] # Last known position
            if t < c.steps:
                current_position = get_clockhand_next_position(c, current_position, lcm_value)
            position_map[key].append(current_position)

    logger.debug(f"Final position map for clockhands: \n{position_map}")
    return crossings.count_hand_crossings(position_map, lcm_value)


def solve_part3(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")
    return -1