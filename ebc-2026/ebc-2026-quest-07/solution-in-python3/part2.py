from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common

def solve_part2(filename):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    energy_map, connections_map = common.get_cloud_maps(text)

    start_id = common.get_cloud_start_id(connections_map)
    initial_energy = 10

    common.disperse_energy(energy_map, connections_map, start_id, initial_energy)

    logger.debug(f"Energy Map: {energy_map}")
    
    return common.get_total_energy_of_all_clouds(energy_map)