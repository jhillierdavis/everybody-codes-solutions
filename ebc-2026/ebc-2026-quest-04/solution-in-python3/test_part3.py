import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_example_additional = "Part3-Example-Input-Additional.txt"
input_example_additional_debug = "Part3-Example-Input-Additional-Debug.txt"
input_full = "Part3-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2998),
        pytest.param(input_example_additional, 3004),
        pytest.param(input_example_additional_debug, 6232480),
        pytest.param(input_full, 7106835), # Not: 7077917, 7060881
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value