import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_full = "Part3-Full-Input.txt"

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("ISO2-3 23", False),
        pytest.param("ISO2-978 99", True),
        #pytest.param(input_full, -1),
    ],    
)
def test_is_min_value(input, expected):
    value = part3.to_value(input)
    actual = part3.is_min_value(input, value)
    assert expected == actual

#@pytest.mark.skip(reason="Ignore as slow!")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 50987),
        pytest.param(input_full, 434479),
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value