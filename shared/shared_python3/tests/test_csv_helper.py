import pytest

from helpers import csv_helper

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("0,1,2,3,4,5", [0,1,2,3,4,5])
    ]
)
def test_to_int_list(input, expected):
    values = csv_helper.to_int_list(input)
    assert expected == values