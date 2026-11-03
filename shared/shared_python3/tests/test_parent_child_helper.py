import pytest

from helpers import parent_child_helper

test_mapping = {
    "A": {"B", "C"},
    "B": {"D"},
    "C": {'E', 'F'},
    "D": {'E'},
    "E": {'G'},
    "F": {'H'},
    "X": {'Y'}
}

@pytest.mark.parametrize(
    "input, target, expected",
    [
        pytest.param(test_mapping, 'A', set()), # Empty set
        pytest.param(test_mapping, 'Z', set()), # Parent (key) not present in the mapping
        pytest.param(test_mapping, 'F', {"A", "C"}),
        pytest.param(test_mapping, 'E', {"A", "B", "C", "D"}),
        pytest.param(test_mapping, 'H', {'A', 'C', 'F'}),
        pytest.param(test_mapping, 'Y', {'X'}),
    ],    
)
def test_get_all_unique_ancestors_of_child(input, target, expected):
    values = parent_child_helper.get_all_unique_ancestors_of_child(input, target)    
    assert values == expected


@pytest.mark.parametrize(
    "input, target, expected",
    [
        pytest.param(test_mapping, 'Z', set()), # Empty set
        pytest.param(test_mapping, 'A', {'B', 'C', 'D', 'E', 'F', 'G', 'H'}),
        pytest.param(test_mapping, 'X', {'Y'}),
    ],    
)
def test_get_all_unique_descendent_references_for_parent(input, target, expected):
    values = parent_child_helper.get_all_unique_descendent_references_for_parent(input, target)
    assert values == expected