import pytest

import part1

input_example = "Part1-Example-Input.txt"
input_example_extra_1 = "Part1-Example-Input-Extra-1.txt"
input_example_extra_2 = "Part1-Example-Input-Extra-2.txt"
input_full = "Part1-Full-Input.txt"

@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 5),
        pytest.param(input_example_extra_1, 7),
        pytest.param(input_example_extra_2, 9),
        pytest.param(input_full, 26),
    ],    
)
def test_solve_part1(filename, expected):
    value = part1.solve_part1(filename)    
    assert expected == value