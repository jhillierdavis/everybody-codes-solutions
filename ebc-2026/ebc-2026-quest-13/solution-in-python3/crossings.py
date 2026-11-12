from itertools import combinations
from math import floor, ceil


def count_hand_crossings(
    hand_positions: dict[tuple[int, int], list[int]],
    clock_size: int = 12,
    step_size: int = 1,
) -> int:
    """
    Count the total number of pairwise hand crossings ("clicks").

    A click occurs when two hands occupy the same position at any
    time t in a sampling interval:

        0 < t <= step_size

    excluding a shared start position (t = 0).

    The clock is treated as a circular domain of size clock_size.

    Parameters
    ----------
    hand_positions
        Dictionary:
            (hand_id, rate) -> [positions...]

        rate > 0 : clockwise
        rate < 0 : counter-clockwise
        rate = 0 : stationary

    clock_size
        Size of clock (e.g. 12, 24, 315)

    step_size
        Duration represented by each interval.

    Returns
    -------
    int
        Total number of clicks.
    """

    if not hand_positions:
        return 0

    tick_count = len(next(iter(hand_positions.values())))

    if tick_count < 2:
        return 0

    def signed_delta(
        start: int,
        end: int,
        rate: int,
    ) -> float:
        """
        Signed movement during one interval.

        Positive values represent clockwise motion.
        Negative values represent counter-clockwise motion.
        """

        if rate > 0:
            return (end - start) % clock_size

        if rate < 0:
            return -((start - end) % clock_size)

        return 0.0

    clicks = 0
    hands = list(hand_positions.items())

    for t in range(tick_count - 1):

        for ((_, rate_a), positions_a), ((_, rate_b), positions_b) in combinations(
            hands, 2
        ):

            a0 = positions_a[t]
            a1 = positions_a[t + 1]

            b0 = positions_b[t]
            b1 = positions_b[t + 1]

            d_a = signed_delta(a0, a1, rate_a)
            d_b = signed_delta(b0, b1, rate_b)

            relative_start = a0 - b0
            relative_speed = d_a - d_b

            #
            # If relative speed is zero, the hands never change
            # their separation during this interval.
            #
            if relative_speed == 0:
                continue

            #
            # Solve:
            #
            #   (a0 + d_a*τ) - (b0 + d_b*τ) = k * clock_size
            #
            # giving
            #
            #   τ = (k*clock_size - relative_start)
            #       / relative_speed
            #
            # We need any solution satisfying:
            #
            #   0 < τ <= step_size
            #
            # τ = 0 does NOT count.
            #

            lower = (
                relative_start
                / clock_size
            )

            upper = (
                relative_start
                + relative_speed * step_size
            ) / clock_size

            k_min = floor(min(lower, upper)) - 1
            k_max = ceil(max(lower, upper)) + 1

            click_found = False

            for k in range(k_min, k_max + 1):

                tau = (
                    k * clock_size - relative_start
                ) / relative_speed

                if 0 < tau <= step_size:
                    click_found = True
                    break

            if click_found:
                clicks += 1

    return clicks