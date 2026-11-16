from helpers import logging_helper, file_helper, grid_helper

logger = logging_helper.get_logger_instance()

def find_all_target_positions(grid: list[list], target: str = 'S') -> set((int, int)):
    """Find all the the start (e.g. 'S') cell."""
    positions = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                positions.add((r,c))                
    return positions


def solve_part1(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

    grid2d = grid_helper.to_grid2d(text)

    sp = find_all_target_positions(grid2d.grid, 'S')
    #start = sp[0]
    waypoints = find_all_target_positions(grid2d.grid, '@')
    ep = find_all_target_positions(grid2d.grid, 'E')
    #end = ep[0]

    logger.debug(f"waypoints={waypoints} sp={sp}, ep={ep}")

    shortest_path = grid_helper.find_shortest_path_with_waypoints(grid2d.grid)
    return len(shortest_path) - 1