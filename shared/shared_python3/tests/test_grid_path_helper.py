import pytest

from helpers import grid_path_helper, grid_helper, file_helper

input_example = "EBC-2026-Quest-17-Part1-Example-Input.txt"
input_full = "EBC-2026-Quest-17-Part1-Full-Input.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 21), 
        pytest.param(input_full, 166),
    ],    
)
def test_solve_part1(filename, expected):
    text = file_helper.get_text(filename)
    grid2d = grid_helper.to_grid2d(text)

    start = (0,0)
    finish = (len(grid2d.grid) - 1, len(grid2d.grid[0]) - 1)

    distance, path = grid_path_helper.shortest_path(grid2d.grid, start, finish, traversable='#')
    assert expected == distance