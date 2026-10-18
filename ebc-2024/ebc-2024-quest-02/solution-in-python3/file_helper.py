from pathlib import Path


def get_text(filename):
    text = Path(filename).read_text(encoding="utf-8")    
    return text


def get_text_sections(filename):
    text = get_text(filename)
    sections = text.strip().split('\n\n')
    return sections