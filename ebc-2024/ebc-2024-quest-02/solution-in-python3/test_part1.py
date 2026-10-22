import pytest

import part1

#input_example = "EBC-2024-Quest-00_Input-Example.txt"
#input_full = "EBC-2024-Quest-00_Input-Full.txt"

#@pytest.mark.skip(reason="Ignore for now!")
@pytest.mark.parametrize(
    "words, sentence, expected",
    [
        pytest.param("THE,OWE,MES,ROD,HER", "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE", 4),
        pytest.param("THE,OWE,MES,ROD,HER", "THE FLAME SHIELDED THE HEART OF THE KINGS", 3),
        pytest.param("THE,OWE,MES,ROD,HER", "POWE PO WER P OWE R", 2),
        pytest.param("THE,OWE,MES,ROD,HER", "THERE IS THE END", 3),
        pytest.param("ID","INCIDIDUNT", 2), # Ensure multiple occurances counted!
        pytest.param("LOR,LL,SI,OR,ID,ME,EA", "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM.", 28),
    ],    
)
def test_solve_part1(words, sentence, expected):
    value = part1.solve_part1(words, sentence)    
    assert expected == value
