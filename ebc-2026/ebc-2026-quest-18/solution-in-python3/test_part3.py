import pytest

import part3

input_example_part2 = "Part2-Example-Input.txt"
input_full_part2 = "Part2-Full-Input.txt"
input_full = "Part3-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, 205),
        pytest.param(input_full_part2, 2336315),
        pytest.param(input_full, 927624576642798),
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value