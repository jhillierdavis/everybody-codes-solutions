from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common

global exploded
exploded = set()

def disperse_energy_with_explosions(energy_map, connections_map, cloud_id, energy_value, limit):
    if energy_value <= 0:
        return

    #logger.debug(f"Dispersing energy {energy_value} to cloud {cloud_id}")

    energy_map[cloud_id] += energy_value
    logger.debug(f"Cloud {cloud_id} impulse with strength: {energy_value}: energy: {energy_map[cloud_id]}")
    if energy_map[cloud_id] >= limit:
        logger.debug(f"Cloud {cloud_id} exploded with energy {energy_map[cloud_id]}")
        energy_value = 10
        exploded.add(cloud_id)

    for connection in connections_map[cloud_id]:
        if connection in exploded:
            continue
        disperse_energy_with_explosions(energy_map, connections_map, connection, energy_value -1, limit)


def get_total_energy_excluding_exploded_clouds(energy_map):
    total_energy = 0
    for cloud_id, energy in energy_map.items():
        if cloud_id not in exploded:
            total_energy += energy
    return total_energy
    

def solve_part3(filename, limit):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")

    energy_map, connections_map = common.get_cloud_maps(text)

    start_id = 2
    initial_energy = 10

    global exploded
    exploded = set()
    disperse_energy_with_explosions(energy_map, connections_map, start_id, initial_energy, limit)

    logger.debug(f"Energy Map: {energy_map}")
    
    return get_total_energy_excluding_exploded_clouds(energy_map)