import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_example_debug = "Part2-Example-Input-Debug.txt"
input_full = "Part2-Full-Input.txt"
input_example_debug_clock_099 = "Part2-Example-Input-Debug-Clock-099.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_debug_clock_099, 4),
    ],    
)
def test_solve_for_clockhands(filename, expected):
    value = part2.solve_for_clockhands(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 21),
        pytest.param(input_example_debug, 135370), # 135370 !
        pytest.param(input_full, 150881), # Not 147539 (although 1st char & length correct), not 112388
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value