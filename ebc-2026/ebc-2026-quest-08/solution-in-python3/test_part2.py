import pytest

import part2

input_example = "Part2-Example-Input.txt"
input_full = "Part2-Full-Input.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 32),
    ],    
)
def test_count_unshaded_trees_to_south_east(filename, expected):
    value = part2.count_unshaded_trees_to_south_east(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 32),
    ],    
)
def test_count_unshaded_trees_to_south_west(filename, expected):
    value = part2.count_unshaded_trees_to_south_west(filename)    
    assert expected == value

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 30),
    ],    
)
def test_count_unshaded_trees_to_north_east(filename, expected):
    value = part2.count_unshaded_trees_to_north_east(filename)    
    assert expected == value

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 32),
    ],    
)
def test_count_unshaded_trees_to_east(filename, expected):
    value = part2.count_unshaded_trees_to_east(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 29),
    ],    
)
def test_count_unshaded_trees_to_west(filename, expected):
    value = part2.count_unshaded_trees_to_west(filename)    
    assert expected == value



@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 32),
    ],    
)
def test_count_unshaded_trees_to_north_west(filename, expected):
    value = part2.count_unshaded_trees_to_north_west(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 187),
        pytest.param(input_full, 1001), # Close: 1053
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve_part2(filename)    
    assert expected == value