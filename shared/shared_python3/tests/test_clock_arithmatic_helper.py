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

@pytest.mark.parametrize(
    "value, max_value",
    [
        pytest.param(-1, 12),
        pytest.param(1, -12),
        pytest.param(-1, -12),
    ],
)
def test_get_clock_value_with_invalid_input(value, max_value):
    with pytest.raises(ValueError, match="value and max_value must be non-negative"):
        clock.get_clock_value(value, max_value)