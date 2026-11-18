import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 94),
        pytest.param(input_full, 6240),
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value