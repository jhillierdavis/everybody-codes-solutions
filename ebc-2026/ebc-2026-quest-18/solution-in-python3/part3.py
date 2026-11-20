from operator import ne

from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


def legacy_calculate_areas(xyz_list):
    last = None
    next = None
    area = 0
    # xyz_list is now passed as an argument, no need to create it here
    fast_forward = 0
    for i, (x, y, w) in enumerate(xyz_list):
        if fast_forward > 0:
            fast_forward -= 1
            continue

        if not last:
            last = (x, y, w)
            continue

        last_x, last_y, last_w = last

        rect_area = 0
        for j in range(i, len(xyz_list)):
            future_y = xyz_list[j][1]  
            if future_y >= last_y:
                future_x = xyz_list[j][0]
                rect_area = (last_y) * (future_x - last_x)
                next = (xyz_list[j][0], xyz_list[j][1], xyz_list[j][2])
                fast_forward = j
                break
        if fast_forward == 0:
            rect_area = last_y * last_w
            if i < len(xyz_list)-1:
                next = (xyz_list[i+1][0], xyz_list[i+1][1], xyz_list[i+1][2])   
        logger.debug(f"i={i}, Last: {last}, Next: {next}, rect_area={rect_area}")
        area += rect_area
        last = next

    return area


def x_calculate_areas(xyz_list):
    area = 0
    last_position = None
    for i, (x, y, w) in enumerate(xyz_list):
        bridging_area = 0
        bar_area = (y * w)
        area += bar_area
        if last_position:
            y_min = min(last_position[1], y)
            bridging_area = y_min * (x - last_position[0])
            area += bridging_area
        last_position = (x+w, y)
        logger.debug(f"i={i},  x={x}, y={y}, w={w}, bar_area={bar_area}, bridging_area={bridging_area if last_position else 0}, total_area={area}")
    return area


def get_next_equal_or_higher_y_value(xyz_list, start_index, y_value):
    for i in range(start_index, len(xyz_list)):
        if xyz_list[i][1] >= y_value:
            return xyz_list[i]
    return None

def get_next_largest_y_value(xyz_list, start_index):
    largest_y = None
    for i in range(start_index, len(xyz_list)):
        if largest_y is None or xyz_list[i][1] > largest_y[1]:
            largest_y = xyz_list[i]
    return largest_y


def calculate_areas(xyz_list):
    area = 0
    #last_position = None
    fast_forward = None
    for i, (x, y, w) in enumerate(xyz_list):
        if fast_forward:
            if fast_forward == (x,y,w):
                fast_forward = None
            else:
                continue

        next_equal_or_higher_y_value = get_next_equal_or_higher_y_value(xyz_list, i+1, y)
        next_largest_y_value = get_next_largest_y_value(xyz_list, i+1)
        if next_equal_or_higher_y_value:
            bar_area = y * (next_equal_or_higher_y_value[0] - x)
            area += bar_area
            #logger.debug(f"i={i}, x={x}, y={y}, w={w}, next_equal_or_higher_y_value={next_equal_or_higher_y_value} bar_area={bar_area} area={area}")
            fast_forward = next_equal_or_higher_y_value
        elif next_largest_y_value:
            bar_area = (y * w) + (next_largest_y_value[1] * (next_largest_y_value[0] - (x+w)))
            area += bar_area
            fast_forward = next_largest_y_value
        else:
            bar_area = (y * w)
            area += bar_area
            #logger.debug(f"i={i}, x={x}, y={y}, w={w}, no next higher or largest y value found, bar_area={bar_area}, area={area}")
    return area




def solve_part3(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    x_list = []
    y_list = []
    w_list = []
    for line in text.splitlines():
        #logger.debug(f"Looking at line: {line}")
        parts = line.split(" ")
        if len(parts) == 3:
            x_list.append(parts[0].removeprefix("x="))
            y_list.append(parts[1].removeprefix("y="))
            w_list.append(parts[2].removeprefix("width="))
    
    logger.debug(f"x_list: {x_list}")
    logger.debug(f"y_list: {y_list}")
    logger.debug(f"w_list: {w_list}")

    xyz_list = list(zip(map(int, x_list), map(int, y_list), map(int, w_list)))
    area = calculate_areas(xyz_list)

    return area