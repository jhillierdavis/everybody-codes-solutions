import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 6),
        pytest.param(input_full, -1), # Not 1518 (1st char & length correct), 1524, 1508, 1510
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value