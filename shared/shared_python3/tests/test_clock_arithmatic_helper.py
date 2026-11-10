import pytest

from helpers import clock_arithmatic_helper as clock


@pytest.mark.parametrize(
    "value, max_value, expected",
    [
        pytest.param(1, 12, 1),
        pytest.param(12, 12, 12),
        pytest.param(13, 12, 1),
        pytest.param(24, 12, 12),
    ],    
)
def test_get_clock_value(value, max_value, expected):
    result = clock.get_clock_value(value, max_value)
    assert expected == result