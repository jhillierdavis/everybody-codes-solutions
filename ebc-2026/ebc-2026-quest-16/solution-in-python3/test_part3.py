import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_full = "Part3-Full-Input.txt"


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, size, expected",
    [
        pytest.param(input_example, 100, 135154),
        pytest.param(input_full, 100, -1),
    ],    
)
def test_solve_part3(filename, size, expected):
    value = part3.solve_part3(filename, size)    
    assert expected == value