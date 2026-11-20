def fill_horizontal(grid):
    """
    Replace '.' cells that are horizontally between '#' cells with '='.

    Args:
        grid: List[str] or List[List[str]]

    Returns:
        List[str]
    """
    result = []

    for row in grid:
        chars = list(row)
        n = len(chars)

        i = 0
        while i < n:
            if chars[i] == '#':
                j = i + 1

                # Find next '#'
                while j < n and chars[j] != '#':
                    j += 1

                if j < n:  # Found another '#'
                    for k in range(i + 1, j):
                        if chars[k] == '.':
                            chars[k] = '='

                i += 1
            else:
                i += 1

        result.append(''.join(chars))

    return result


def count_filled_cells(grid, x_max, y_max):
    count = 0
    for c in range(x_max + 1):
        for r in range(y_max + 1):
            if grid[r][c] == '=' or grid[r][c] == '#':
                count += 1
    return count