from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()


from dataclasses import dataclass
from typing import List


@dataclass
class Rectangle:
    x: int       # left column
    y: int       # top row
    width: int
    height: int


def find_rectangles(grid: List[str]) -> List[Rectangle]:
    """
    Find all rectangular regions of '#' in a grid.

    Returns a list of Rectangle(x, y, width, height).
    """
    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    rectangles = []

    for y in range(rows):
        for x in range(cols):
            logger.debug(f"Checking cell ({x}, {y}): {grid[y][x]}")
            if grid[y][x] != "#" or visited[y][x]:
                continue

            # Determine rectangle width
            width = 0
            while x + width < cols and grid[y][x + width] == "#":
                width += 1

            # Determine rectangle height
            height = 0
            while y + height < rows and grid[y + height][x] == "#":
                height += 1

            # Validate rectangle is completely filled
            for yy in range(y, y + height):
                for xx in range(x, x + width):
                    if grid[yy][xx] != "#":
                        raise ValueError(
                            f"Non-rectangular shape found at ({x}, {y})"
                        )

            # Mark visited
            for yy in range(y, y + height):
                for xx in range(x, x + width):
                    visited[yy][xx] = True

            rectangles.append(
                Rectangle(
                    x=x,
                    y=y,
                    width=width,
                    height=height,
                )
            )

    return rectangles


def solve_part1(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols = grid_helper.to_grid(text)
    logger.debug(f"Grid:\n {grid_helper.to_string(grid)}")

    rectangles = find_rectangles(grid)
    logger.debug(f"Rectangles: {rectangles}")

    return sum(min(r.width, r.height) for r in rectangles)