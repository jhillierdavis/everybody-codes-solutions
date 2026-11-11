from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

from dataclasses import dataclass
from collections import deque
from typing import List, Set, Tuple


@dataclass(frozen=True)
class Rectangle:
    x: int
    y: int
    width: int
    height: int


@dataclass(frozen=True)
class LShape:
    x: int
    y: int
    width: int                 # bounding box width
    height: int                # bounding box height
    horizontal_thickness: int
    vertical_thickness: int
    orientation: str           # top_left, top_right, bottom_left, bottom_right


def find_shapes(grid: List[str]) -> tuple[List[Rectangle], List[LShape]]:
    """
    Find all rectangles and L-shapes in a grid.

    Returns:
        (rectangles, l_shapes)
    """

    if not grid:
        return [], []

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    rectangles = []
    l_shapes = []

    def neighbours(x: int, y: int):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < cols and 0 <= ny < rows:
                yield nx, ny

    def get_component(start_x: int, start_y: int) -> Set[Tuple[int, int]]:

        component = set()

        queue = deque([(start_x, start_y)])
        visited[start_y][start_x] = True

        while queue:
            x, y = queue.popleft()
            component.add((x, y))

            for nx, ny in neighbours(x, y):
                if (
                    grid[ny][nx] == "#"
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    queue.append((nx, ny))

        return component

    def classify_rectangle(
        cells: Set[Tuple[int, int]]
    ) -> Rectangle | None:

        min_x = min(x for x, _ in cells)
        max_x = max(x for x, _ in cells)

        min_y = min(y for _, y in cells)
        max_y = max(y for _, y in cells)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        if len(cells) != width * height:
            return None

        return Rectangle(
            x=min_x,
            y=min_y,
            width=width,
            height=height,
        )

    def classify_l_shape(
        cells: Set[Tuple[int, int]]
    ) -> LShape | None:

        min_x = min(x for x, _ in cells)
        max_x = max(x for x, _ in cells)

        min_y = min(y for _, y in cells)
        max_y = max(y for _, y in cells)

        bbox_width = max_x - min_x + 1
        bbox_height = max_y - min_y + 1

        # Rectangles are not L-shapes
        if len(cells) == bbox_width * bbox_height:
            return None

        orientations = (
            "top_left",
            "top_right",
            "bottom_left",
            "bottom_right",
        )

        for h_thickness in range(1, bbox_height + 1):
            for v_thickness in range(1, bbox_width + 1):

                for orientation in orientations:

                    expected = set()

                    if orientation == "top_left":

                        # vertical arm
                        for y in range(min_y, max_y + 1):
                            for x in range(
                                min_x,
                                min_x + v_thickness
                            ):
                                expected.add((x, y))

                        # horizontal arm
                        for y in range(
                            min_y,
                            min_y + h_thickness
                        ):
                            for x in range(min_x, max_x + 1):
                                expected.add((x, y))

                    elif orientation == "top_right":

                        # vertical arm
                        for y in range(min_y, max_y + 1):
                            for x in range(
                                max_x - v_thickness + 1,
                                max_x + 1
                            ):
                                expected.add((x, y))

                        # horizontal arm
                        for y in range(
                            min_y,
                            min_y + h_thickness
                        ):
                            for x in range(min_x, max_x + 1):
                                expected.add((x, y))

                    elif orientation == "bottom_left":

                        # vertical arm
                        for y in range(min_y, max_y + 1):
                            for x in range(
                                min_x,
                                min_x + v_thickness
                            ):
                                expected.add((x, y))

                        # horizontal arm
                        for y in range(
                            max_y - h_thickness + 1,
                            max_y + 1
                        ):
                            for x in range(min_x, max_x + 1):
                                expected.add((x, y))

                    else:  # bottom_right

                        # vertical arm
                        for y in range(min_y, max_y + 1):
                            for x in range(
                                max_x - v_thickness + 1,
                                max_x + 1
                            ):
                                expected.add((x, y))

                        # horizontal arm
                        for y in range(
                            max_y - h_thickness + 1,
                            max_y + 1
                        ):
                            for x in range(min_x, max_x + 1):
                                expected.add((x, y))

                    if expected == cells:
                        return LShape(
                            x=min_x,
                            y=min_y,
                            width=bbox_width,
                            height=bbox_height,
                            horizontal_thickness=h_thickness,
                            vertical_thickness=v_thickness,
                            orientation=orientation,
                        )

        return None

    for y in range(rows):
        for x in range(cols):

            if grid[y][x] != "#" or visited[y][x]:
                continue

            component = get_component(x, y)

            rectangle = classify_rectangle(component)

            if rectangle is not None:
                rectangles.append(rectangle)
                continue

            l_shape = classify_l_shape(component)

            if l_shape is not None:
                l_shapes.append(l_shape)

    return rectangles, l_shapes



def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)
    grid = grid2d.grid
    logger.debug(f"Grid:\n {grid_helper.to_string(grid)}")

    rectangles, l_shapes = find_shapes(grid)

    #for l in l_shapes: 
    #logger.debug(f"L-Shape: {l}, Width: {l.width}, Height: {l.height}, Orientation: {l.orientation}, Horizontal thickness: {l.horizontal_thickness}, Vertical thickness: {l.vertical_thickness}")
   
    return sum(min(r.width, r.height) for r in rectangles) + sum(min(min(l.width, l.height), (l.horizontal_thickness + l.vertical_thickness) ) for l in l_shapes)