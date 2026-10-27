import pytest

from helpers import interval_helper

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([(1,3), (2,6), (8,10), (9,12), (15,18)], [(1,6), (8,12), (15,18)])
    ]
)
def test_merge_overlapping(input, expected):
    value = interval_helper.merge_overlapping(input)    
    assert expected == value