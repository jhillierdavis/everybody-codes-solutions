# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

"""
def solve_part1(words, sentence):
    #return count_overlapping_occurrences(sentence, words)
    word_list = words.split(',')
    for w in word_list:
        logger.debug(f"w={w} count={sentence.count(w)}")
    return 0
    #return sum([sentence.count(w) for w in word_list])
"""

def solve_part1(words, sentence):
    word_list = words.split(',')

    #sentence_word_list = sentence.split()
    #logger.debug(f"sentence_word_list={sentence_word_list}")

    ans = 0
    for w in word_list:
        count = sentence.count(w)    
        logger.debug(f"w={w} count={count}")
        ans += count          

    return ans
