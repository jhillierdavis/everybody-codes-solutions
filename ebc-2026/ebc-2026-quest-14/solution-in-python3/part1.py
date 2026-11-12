from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

def count_unique_boundaries(grid):
    rows = len(grid)
    cols = len(grid[0])

    total = 0
    processed = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for ch in sorted({cell for row in grid for cell in row}):
        processed.add(ch)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != ch:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Window frame
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        total += 1
                        continue

                    neighbour = grid[nr][nc]

                    # Different piece and not yet processed
                    if neighbour != ch and neighbour not in processed:
                        total += 1

    return total


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)

    return count_unique_boundaries(grid2d.grid)