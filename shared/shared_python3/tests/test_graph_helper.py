import pytest

from helpers import graph_helper

# Example usage of graph_helper functions: see https://everybody.codes/event/2026/quests/2

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("D<C B<E C>A A>B A<E D<A C>B D<B C>E D<E", ['C','E','A','B','D']),
        pytest.param("C>D E>B C>A A>B E>A A>D C>B B>D C>E E>D", ['C','E','A','B','D']),
        pytest.param("C>A A>B E>A B>D C>E", ['C','E','A','B','D']),
        pytest.param("4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5", ['3','5','1','2','4']),
        pytest.param("2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5", ['3','5','1','2','4']),
        pytest.param("3>1 1>2 1<5 4<2 3>5", ['3','5','1','2','4']),
        pytest.param("4>1 2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3", ['4','3','5','2','1']),
        pytest.param("2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3", ['4','3','5','2','1']),
        pytest.param("2>1 2<5 3>1 4>3 2<4 5<3", ['4','3','5','2','1']),
        pytest.param("5>1 5>2 4>1 2<4 3>2 3<4 1>2 3>5 1<3 4>5", ['4','3','5','1','2']),
        pytest.param("5>1 5>2 4>1 3>2 3<4 1>2 3>5 1<3 4>5", ['4','3','5','1','2']),
        pytest.param("5>1 3<4 1>2 3>5", ['4','3','5','1','2']),
    ]
)
def test_get_nodes_by_precedence_largest_first(input, expected):
    values = graph_helper.get_nodes_by_precedence_largest_first(input)
    assert expected == values


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("D<C B<E C>A A>B A<E D<A C>B D<B C>E D<E", ['D', 'B', 'A', 'E', 'C']),
        pytest.param("C>D E>B C>A A>B E>A A>D C>B B>D C>E E>D", ['D', 'B', 'A', 'E', 'C']),
        pytest.param("C>A A>B E>A B>D C>E",['D', 'B', 'A', 'E', 'C']),
    ]
)
def test_get_nodes_by_precedence_smallest_first(input, expected):
    values = graph_helper.get_nodes_by_precedence(input)
    assert expected == values