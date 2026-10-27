import pytest

import file_helper


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param("File-Helper-Text-Sections.txt", ['section one\nmore of section one', 'section two\ncontinues here']),
    ],    
)
def test_get_text_sections(filename, expected):
    value = file_helper.get_text_sections(filename)
    assert expected == value