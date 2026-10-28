import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


from helpers import file_helper, graph_helper

def solve(filename):
    text = file_helper.get_text(filename)

    ans = 0
    for l in text.splitlines():
        result = graph_helper.get_nodes_by_precedence_largest_first(l)
        value = "".join(v for v in result)
        ans += int(value)

    return ans