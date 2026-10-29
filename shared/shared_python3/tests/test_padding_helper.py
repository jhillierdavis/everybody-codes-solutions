import pytest

from helpers import padding_helper

@pytest.mark.parametrize(
    "input, size, expected",
    [
        pytest.param("13", 3 , "313"),
        pytest.param("34", 6 , "343434"),
        pytest.param("789", 7 , "9789789"),
    ],    
)
def test_prefix_pad(input, size, expected):
    value = padding_helper.prefix_pad(input, size)    
    assert expected == value