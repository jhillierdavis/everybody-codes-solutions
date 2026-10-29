import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("ISO-3210 7654", 222),
        pytest.param("ISO-8742 2468", 1252),
        pytest.param("ISO-1 1111", 4),
        pytest.param("ISO-13 777", 77),
        pytest.param("ISO-34 140856", 1416),
        pytest.param("ISO-789 2465112", 1158390),
        pytest.param("ISO-2341 945", 102),
    ],    
)
def test_to_value(input, expected):
    value = part2.to_value(input)    
    assert expected == value

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1161463),
        pytest.param(input_full, 20233862655),
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value