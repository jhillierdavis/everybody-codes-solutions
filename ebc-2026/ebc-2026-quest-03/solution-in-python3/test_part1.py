import pytest

import part1

input_example = "Part1-Example-Input.txt"
input_full = "Part1-Full-Input.txt"

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("ISO-3210 7654", 222),
        pytest.param("ISO-8742 2468", 1252),
        pytest.param("ISO-1111 1111", 4),
    ],    
)
def test_to_value(input, expected):
    value = part1.to_value(input)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1478),
        pytest.param(input_full, 12065),
    ],    
)
def test_solve_part1(filename, expected):
    value = part1.solve_part1(filename)    
    assert expected == value