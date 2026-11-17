import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, size, expected",
    [
        pytest.param(input_example, 10, 1053),
        #pytest.param(input_full, 10, 24675718),
    ],    
)
def test_solve_part2(filename, size, expected):
    value = part2.solve_part2(filename, size)    
    assert expected == value