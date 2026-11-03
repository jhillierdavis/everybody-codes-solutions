import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_example_additional = "Part2-Example-Additional-Input.txt"
input_full = "Part2-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1316),
        pytest.param(input_example_additional, 1214633),
        #pytest.param(input_full, 125719396),
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value