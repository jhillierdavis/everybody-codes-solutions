
from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

def text_to_input_map(text):
    results_map = {}
    for line in text.splitlines():
        #logger.debug(f"Line: {line}")
        parts = line.split(',')
        id = int(parts[0].split('=')[1])
        growth = int(parts[1].split('=')[1])
        limit    = int(parts[2].split('=')[1])
        results_map[id] = (growth, limit)

    return results_map
    
    