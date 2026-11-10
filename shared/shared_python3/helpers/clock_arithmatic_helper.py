def get_clock_value(value, max_value):
    """
    Get the 'clock value' (using cyclic arithmetic) of a given value with respect to a maximum value.
    If the value is divisible by the max_value, return max_value.
    Otherwise, return the remainder of value divided by max_value.
    """
    return (value % max_value) or max_value