import pytest

import part3


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param("Part3-Example-Input.txt", 10),
        pytest.param("Part3-Full-Input.txt", 11972), # Not 11967!
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve(filename)    
    assert expected == value    