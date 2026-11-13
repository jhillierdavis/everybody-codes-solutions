import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_full = "Part3-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, max_collisions, expected",
    [
        #pytest.param("Part2-Example-Input.txt", 10, 53),
        pytest.param("Part2-Example-Input.txt", 10000, 50000),
        #pytest.param("Part2-Full-Input.txt", 10000, 136520),
        #pytest.param(input_example, 1000000000, 13314695352588),
        #pytest.param(input_full, 1000000000, -1),
    ],    
)
def test_solve_part3(filename, max_collisions, expected):
    value = part3.solve_part3(filename, max_collisions)    
    assert expected == value