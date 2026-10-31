import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_full = "Part3-Full-Input.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 14),
        pytest.param(input_full, 9865),
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value