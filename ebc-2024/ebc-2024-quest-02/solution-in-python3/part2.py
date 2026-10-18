import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


import re

def find_word_positions(paragraph, word, case_sensitive=False):
    """
    Find all positions where a word appears in a paragraph.

    Args:
        paragraph (str): The text to search.
        word (str): The word to find.
        case_sensitive (bool): Whether matching should be case-sensitive.

    Returns:
        list: Starting positions of all matches.
    """
    flags = 0 if case_sensitive else re.IGNORECASE

    # Match whole words only
    pattern = r'\b' + re.escape(word) + r'\b'

    return [match.start() for match in re.finditer(pattern, paragraph, flags)]


def count_runic_symbols(words, sentence):
    import interval_helper

    s = sentence
    logger.debug(f"s={s}")

    index_list = []
    ans = 0
    for w in words.split(','):
        """
        count = sentence.count(w) + sentence[::-1].count(w)
        logger.debug(f"count={count} w={w} sentence={sentence}")
        ans += len(w) * count
        """

        #index_list.extend(get_subword_start_end_indexes(w, s))
        #index_list.extend(get_subword_start_end_indexes(w[::-1], s))

        index_list.extend(find_subword_indexes(w, s))
        index_list.extend(find_subword_indexes(w[::-1], s))

        logger.debug(f"w={w} index_list={index_list}")

    merged_intervals = interval_helper.merge_overlapping(index_list)
    logger.debug(f"merged_intervals={merged_intervals}")

    for (start, end) in merged_intervals:
        ans += 1 + (end - start) 

    return ans


def find_subword_indexes(subword:str, text:str) -> list[tuple[int,int]]:

    if not subword:
        raise ValueError("subword must not be empty!")

    result = []

    start = 0

    while True:
        pos = text.find(subword, start)
        if pos == -1:
            break

        result.append((pos, pos + len(subword)-1))

        start = pos + 1 # Advance by one character to allow overlaps

    return result


def get_subword_start_end_indexes(subword, text):
    import re


    index_list = [(m.start(), m.end()) for m in re.finditer(subword, text)]
    return index_list


def solve(filename):
    import file_helper

    sections = file_helper.get_text_sections(filename)

    # split each section into lines
    words = sections[0][6:]
    sentences = sections[1].split('\n')

    logger.debug(f"words={words}")
    logger.debug(f"sentences={sentences}")

    ans = 0
    """
    for s in sentences:
        #count = sum([s.count(w) for w in words])
        #count += sum([s[::-1].count(w) for w in words])
        #logger.debug(f"count={count} for s={s}")
        for w in words:
            count = s.count(w) + s[::-1].count(w)
            ans += len(w) * count
    """

    for s in sentences:
        ans += count_runic_symbols(words, s)
    return ans