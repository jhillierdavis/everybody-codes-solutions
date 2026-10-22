def merge_overlapping(intervals):
    """
    Merge overlapping intervals

    Args:
        intervals: list of interval tuples with integer values: (start, end)
    Returns:
        List of merged interval tuples (start, end)
    """

    if not intervals:
        return []

    # Sort by start value
    sorted_intervals = sorted(intervals, key=lambda x:x[0])

    merged = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start , last_end = merged[-1]

        if start <= last_end: # Overlap detected
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged 