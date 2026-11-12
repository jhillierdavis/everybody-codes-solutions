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