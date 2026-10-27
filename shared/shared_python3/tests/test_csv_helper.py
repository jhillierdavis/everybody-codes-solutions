import pytest

from helpers import csv_helper

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("0,1,2,3,4,5", [0,1,2,3,4,5]),
        pytest.param("27,-1,-99", [27,-1,-99]),
        pytest.param("3, 2,  1, 0 ", [3,2,1,0]),
        pytest.param("", []),
        pytest.param(" ", []),
        #pytest.param("a, b,c ", []), # Ensure ValueError
    ]
)
def test_to_int_list(input, expected):
    values = csv_helper.to_int_list(input)
    assert expected == values


@pytest.mark.parametrize(
    "input, expected",
    [         
        pytest.param('a, b, c', ['a','b','c']), 
        pytest.param('a,b,c', ['a','b','c']), 
        pytest.param('a,b , c', ['a','b','c']), 
        pytest.param('a,    b,c', ['a','b','c']), 
        pytest.param('a b c', ['a b c']),
        pytest.param('solo', ['solo']),
        pytest.param('left, right', ['left', 'right']),
        pytest.param('', []),
    ],    
)
def test_to_list(input:str, expected) -> list:
    assert csv_helper.to_list(input) == expected