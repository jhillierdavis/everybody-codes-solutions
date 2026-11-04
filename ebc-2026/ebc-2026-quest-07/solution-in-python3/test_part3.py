import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_example_debug = "Part3-Example-Debug-Input.txt"
input_full = "Part3-Full-Input.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, limit, expected",
    [
        pytest.param(input_example, 100, 187),
        pytest.param(input_example_debug, 1000000, 34777023),
        pytest.param(input_full, 1000000, 30654897),
    ],    
)
def test_solve_part3(filename, limit, expected):
    value = part3.solve_part3(filename, limit)    
    assert expected == value