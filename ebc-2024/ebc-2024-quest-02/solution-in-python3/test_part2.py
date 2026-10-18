import pytest

import part2

@pytest.mark.parametrize(
    "words, sentence, expected",
    [
        pytest.param("THE,OWE,MES,ROD,HER,QAQ", "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE", 15),
        pytest.param("THE,OWE,MES,ROD,HER,QAQ", "THE FLAME SHIELDED THE HEART OF THE KINGS", 9),
        pytest.param("THE,OWE,MES,ROD,HER,QAQ", "POWE PO WER P OWE R", 6),
        pytest.param("THE,OWE,MES,ROD,HER,QAQ", "THERE IS THE END", 7),
        pytest.param("THE,OWE,MES,ROD,HER,QAQ", "QAQAQ", 5)
    ],    
)
def test_count_runic_symbols(words, sentence, expected):
    value = part2.count_runic_symbols(words, sentence)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param("Part2-Example-Input.txt", 42),
        pytest.param("Part2-Full-Input.txt", 5135),
    ],    
)
def test_solve_part2(filename, expected):
    value = part2.solve(filename)    
    assert expected == value


