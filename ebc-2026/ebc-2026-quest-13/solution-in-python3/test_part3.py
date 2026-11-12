from shutil import move

import pytest

import part3

input_example = "Part3-Example-Input.txt"
input_full = "Part3-Full-Input.txt"

clock_001 = """hands 10:10:10
direction CW:CW:CW
current 9:0:5
move 5400:0:0
"""

clock_002 = """hands 6:6:6
direction CW:CW:CW
current 1:1:1
move 6240:6240:6240
"""

clock_003 = """hands 9:11:20
direction CW:CCW:CW
current 0:1:17
move 7224:7352:7518
"""

clock_020 = """hands 4:4:32
direction CW:CCW:CCW
current 3:2:25
move 162645:166182:165763
"""

clock_060 = """hands 5:12:23
direction CW:CW:CW
current 3:9:4
move 241272341:247317339:249069750
"""

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(clock_001, 1080),
        pytest.param(clock_002, 0),
        pytest.param(clock_003, 2972),
        pytest.param(clock_020, 164414),
        #pytest.param(clock_060, 76688616), # Slow - skipping for now
    ],    
)
def test_solve_for_clockhands(input, expected):
    value = part3.solve_for_clockhands(input)    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        #pytest.param(input_example, 984329851511),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part3(filename, expected):
    value = part3.solve_part3(filename)    
    assert expected == value