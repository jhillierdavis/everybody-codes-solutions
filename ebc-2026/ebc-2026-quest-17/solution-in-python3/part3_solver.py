from collections import defaultdict

# Clockwise direction order
DIRS = [
    (1, 0),    # East
    (0, 1),    # South
    (-1, 0),   # West
    (0, -1),   # North
]

DIR_INDEX = {d: i for i, d in enumerate(DIRS)}


def build_boundary_edges(grid):
    """
    Create a clockwise-oriented perimeter edge for every exposed cell edge.
    """
    rows = len(grid)
    cols = len(grid[0])

    edges = []

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] != "#":
                continue

            # North edge
            if r == 0 or grid[r - 1][c] == ".":
                edges.append(((c, r), (c + 1, r)))

            # East edge
            if c == cols - 1 or grid[r][c + 1] == ".":
                edges.append(((c + 1, r), (c + 1, r + 1)))

            # South edge
            if r == rows - 1 or grid[r + 1][c] == ".":
                edges.append(((c + 1, r + 1), (c, r + 1)))

            # West edge
            if c == 0 or grid[r][c - 1] == ".":
                edges.append(((c, r + 1), (c, r)))

    return edges


def trace_contour(edges):
    """
    Follow the perimeter using a clockwise wall-following rule.
    Returns the ordered contour vertices.
    """
    outgoing = defaultdict(list)

    for a, b in edges:
        outgoing[a].append(b)

    visited = set()

    start_edge = edges[0]
    current = start_edge

    contour = []

    while current not in visited:

        visited.add(current)

        a, b = current
        contour.append(a)

        incoming_dir = (
            b[0] - a[0],
            b[1] - a[1],
        )

        incoming_idx = DIR_INDEX[incoming_dir]

        best_next = None
        best_turn = None

        for nxt in outgoing[b]:

            outgoing_dir = (
                nxt[0] - b[0],
                nxt[1] - b[1],
            )

            outgoing_idx = DIR_INDEX[outgoing_dir]

            # Smallest clockwise turn keeps the wall on the right
            turn = (outgoing_idx - incoming_idx) % 4

            if best_next is None or turn < best_turn:
                best_next = nxt
                best_turn = turn

        current = (b, best_next)

    return contour


def contour_side_lengths(grid):
    """
    Returns:
      north side length
      east side length
      south side length
      west side length
      perimeter
      north+east route
      south+west route
      shortest route
    """

    edges = build_boundary_edges(grid)

    contour = trace_contour(edges)

    perimeter = len(contour)

    # Extreme contour vertices

    nw = min(contour, key=lambda p: (p[1], p[0]))
    ne = min(contour, key=lambda p: (p[1], -p[0]))
    se = max(contour, key=lambda p: (p[1], p[0]))
    sw = max(contour, key=lambda p: (p[1], -p[0]))

    position = {}

    # First occurrence on contour
    for i, vertex in enumerate(contour):
        if vertex not in position:
            position[vertex] = i

    n = len(contour)

    def distance(start, end):
        return (end - start) % n

    north = distance(position[nw], position[ne])
    east = distance(position[ne], position[se])
    south = distance(position[se], position[sw])
    west = distance(position[sw], position[nw])

    north_east = north + east
    south_west = south + west

    return {
        "north": north,
        "east": east,
        "south": south,
        "west": west,
        "perimeter": perimeter,
        "north_east_path": north_east,
        "south_west_path": south_west,
        "shortest_path": min(north_east, south_west),
        "extremes": {
            "nw": nw,
            "ne": ne,
            "se": se,
            "sw": sw,
        },
    }


if __name__ == "__main__":

    grid = [
        "####.######",
        "#.#.##..#..",
        "##.##.##..#",
        "#.#.###.###",
        "#.###.###.#",
        "###.##.#.##",
    ]

    result = contour_side_lengths(grid)

    print("North:", result["north"])
    print("East :", result["east"])
    print("South:", result["south"])
    print("West :", result["west"])
    print("Perimeter:", result["perimeter"])

    print()
    print("North+East path:", result["north_east_path"])
    print("South+West path:", result["south_west_path"])
    print("Shortest path:", result["shortest_path"])
