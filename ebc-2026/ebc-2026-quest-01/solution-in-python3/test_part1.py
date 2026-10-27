import pytest

import part1

input_example = "Part1-Example-Input.txt"
input_full = "Part1-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 11),
        pytest.param(input_full, 1375),
    ],    
)
def test_solve_part1(filename, expected):
    value = part1.solve_part1(filename)  
    assert expected == value