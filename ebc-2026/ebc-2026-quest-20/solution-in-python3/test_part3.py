import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_example_extra_1 = "Part3-Example-Input-Extra-1.txt"
input_full = "Part3-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 125),
        pytest.param(input_example_extra_1, 693),
        pytest.param(input_full, -1), # Not: 33537 , 33537 , 35A95, 4316A, 43455, 43159
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value