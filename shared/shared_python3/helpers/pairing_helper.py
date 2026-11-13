def get_unique_pairings(values):
    """
    Generate all possible pairings of the given values.
    The number of values must be even.
    
    Returns a list of sets, where each set contains tuples representing unique pairs.
    """
    values = list(values)

    if len(values) % 2 != 0:
        raise ValueError("Number of values must be even")

    def generate(remaining):
        if not remaining:
            return [set()]

        first = remaining[0]
        result = []

        for i in range(1, len(remaining)):
            second = remaining[i]

            pair = tuple(sorted((first, second)))
            rest = remaining[1:i] + remaining[i + 1:]

            for pairing in generate(rest):
                result.append(pairing | {pair})

        return result

    return generate(values)