import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"

@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, max_collisions, expected",
    [
        pytest.param(input_example, 10, 53),
        pytest.param(input_example, 10000, 50000),
        pytest.param(input_full, 10000, 136520),
    ],    
)
def test_solve_part2(filename, max_collisions, expected):
    value = part2.solve_part2(filename, max_collisions)    
    assert expected == value