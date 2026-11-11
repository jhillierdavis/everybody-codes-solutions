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
    width: int
    height: int
    horizontal_thickness: int
    vertical_thickness: int
    orientation: str


@dataclass(frozen=True)
class RectangleWithHole:
    x: int
    y: int
    width: int
    height: int

    hole_x: int
    hole_y: int
    hole_width: int
    hole_height: int


def find_shapes(
    grid: List[str]
) -> tuple[
    List[Rectangle],
    List[LShape],
    List[RectangleWithHole]
]:
    """
    Find all connected shapes in a grid.

    Returns:
        (
            rectangles,
            l_shapes,
            rectangles_with_holes,
        )
    """

    if not grid:
        return [], [], []

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    rectangles = []
    l_shapes = []
    rectangles_with_holes = []

    def neighbours(x: int, y: int):
        for dx, dy in (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < cols and 0 <= ny < rows:
                yield nx, ny

    def get_component(
        start_x: int,
        start_y: int
    ) -> Set[Tuple[int, int]]:

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

    def classify_rectangle_with_hole(
        cells: Set[Tuple[int, int]]
    ) -> RectangleWithHole | None:

        min_x = min(x for x, _ in cells)
        max_x = max(x for x, _ in cells)

        min_y = min(y for _, y in cells)
        max_y = max(y for _, y in cells)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        full_box = {
            (x, y)
            for y in range(min_y, max_y + 1)
            for x in range(min_x, max_x + 1)
        }

        missing = full_box - cells

        if not missing:
            return None

        hole_min_x = min(x for x, _ in missing)
        hole_max_x = max(x for x, _ in missing)

        hole_min_y = min(y for _, y in missing)
        hole_max_y = max(y for _, y in missing)

        hole_width = hole_max_x - hole_min_x + 1
        hole_height = hole_max_y - hole_min_y + 1

        expected_hole = {
            (x, y)
            for y in range(hole_min_y, hole_max_y + 1)
            for x in range(hole_min_x, hole_max_x + 1)
        }

        if expected_hole != missing:
            return None

        expected_shape = full_box - expected_hole

        if expected_shape != cells:
            return None

        return RectangleWithHole(
            x=min_x,
            y=min_y,
            width=width,
            height=height,
            hole_x=hole_min_x,
            hole_y=hole_min_y,
            hole_width=hole_width,
            hole_height=hole_height,
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

        if len(cells) == bbox_width * bbox_height:
            return None

        for horizontal_thickness in range(
            1,
            bbox_height + 1
        ):

            for vertical_thickness in range(
                1,
                bbox_width + 1
            ):

                for orientation in (
                    "top_left",
                    "top_right",
                    "bottom_left",
                    "bottom_right",
                ):

                    expected = set()

                    if orientation == "top_left":

                        for y in range(min_y, max_y + 1):
                            for x in range(
                                min_x,
                                min_x + vertical_thickness
                            ):
                                expected.add((x, y))

                        for y in range(
                            min_y,
                            min_y + horizontal_thickness
                        ):
                            for x in range(
                                min_x,
                                max_x + 1
                            ):
                                expected.add((x, y))

                    elif orientation == "top_right":

                        for y in range(min_y, max_y + 1):
                            for x in range(
                                max_x - vertical_thickness + 1,
                                max_x + 1
                            ):
                                expected.add((x, y))

                        for y in range(
                            min_y,
                            min_y + horizontal_thickness
                        ):
                            for x in range(
                                min_x,
                                max_x + 1
                            ):
                                expected.add((x, y))

                    elif orientation == "bottom_left":

                        for y in range(min_y, max_y + 1):
                            for x in range(
                                min_x,
                                min_x + vertical_thickness
                            ):
                                expected.add((x, y))

                        for y in range(
                            max_y - horizontal_thickness + 1,
                            max_y + 1
                        ):
                            for x in range(
                                min_x,
                                max_x + 1
                            ):
                                expected.add((x, y))

                    else:  # bottom_right

                        for y in range(min_y, max_y + 1):
                            for x in range(
                                max_x - vertical_thickness + 1,
                                max_x + 1
                            ):
                                expected.add((x, y))

                        for y in range(
                            max_y - horizontal_thickness + 1,
                            max_y + 1
                        ):
                            for x in range(
                                min_x,
                                max_x + 1
                            ):
                                expected.add((x, y))

                    if expected == cells:

                        return LShape(
                            x=min_x,
                            y=min_y,
                            width=bbox_width,
                            height=bbox_height,
                            horizontal_thickness=horizontal_thickness,
                            vertical_thickness=vertical_thickness,
                            orientation=orientation,
                        )

        return None

    for y in range(rows):
        for x in range(cols):

            if (
                grid[y][x] != "#"
                or visited[y][x]
            ):
                continue

            component = get_component(x, y)

            rectangle = classify_rectangle(component)
            if rectangle:
                rectangles.append(rectangle)
                continue

            l_shape = classify_l_shape(component)
            if l_shape:
                l_shapes.append(l_shape)
                continue

            rectangle_with_hole = classify_rectangle_with_hole(
                component
            )
            if rectangle_with_hole:
                rectangles_with_holes.append(
                    rectangle_with_hole
                )
                continue



    return (
        rectangles,
        l_shapes,
        rectangles_with_holes,
    )


def solve_part3(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    grid, rows, cols = grid_helper.to_grid(text)
    logger.debug(f"Grid:\n {grid_helper.to_string(grid)}")

    rectangles, l_shapes, rectangles_with_holes = find_shapes(grid)

    sum_r = 0
    for r in rectangles:
        spells = min(r.width, r.height)
        logger.debug(f"Rectangle: {r}, Width: {r.width}, Height: {r.height} spells={spells}")
        sum_r += spells

    sum_l = 0
    for l in l_shapes:
        spells = min(min(l.width, l.height), (l.horizontal_thickness + l.vertical_thickness) )
        logger.debug(f"L-Shape: {l}, Width: {l.width}, Height: {l.height}, Orientation: {l.orientation}, Horizontal thickness: {l.horizontal_thickness}, Vertical thickness: {l.vertical_thickness}, spells={spells}")
        sum_l += spells

    sum_rwh = 0
    for rwh  in rectangles_with_holes:
        spells = min(rwh.width + 1, rwh.height + 1)
        logger.debug(f"Rectangle with hole: {rwh}, Width: {rwh.width}, Height: {rwh.height}, spells={spells}")
        sum_rwh += spells

    logger.debug(f"Sum rectangles: {sum_r}, Sum L-shapes: {sum_l}, Sum rectangles with holes: {sum_rwh}")
    return (
        sum_r
        + sum_l
        + sum_rwh
    )