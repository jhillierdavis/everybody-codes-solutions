from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common


def disperse_energy_with_explosions(energy_map, connections_map, cloud_id, energy_value, limit):
    exploded = set()   
    stage = 1

    map_current_impulse = {}
    map_next_impulse = {}

    map_current_impulse[cloud_id] = [energy_value]

    while map_current_impulse:
        if stage > 100:  # Prevent infinite loops
            logger.warning(f"Stage {stage}: Exceeded maximum stages, stopping to prevent infinite loop.")
            return exploded
        
        for cloud_id, impulse_values in map_current_impulse.items():
            if cloud_id in exploded:
                continue

            for impulse_value in impulse_values:
                next_energy_value =  energy_map.get(cloud_id, 0) + impulse_value
                energy_map[cloud_id] = next_energy_value

            for connection in connections_map.get(cloud_id, []):   
                for impulse_value in impulse_values:
                    map_next_impulse[connection] = map_next_impulse.get(connection, [])
                    new_impulse_value = impulse_value - 1
                    if new_impulse_value > 0:
                        map_next_impulse[connection].append(new_impulse_value)

        # Handle explosions
        for cloud_id in energy_map.keys():
            if cloud_id in exploded:
                continue

            current_energy = energy_map.get(cloud_id, 0)
            if current_energy < limit:
                continue

            #logger.debug(f"Stage {stage}: Cloud {cloud_id} exploded with energy {energy_map.get(cloud_id, 0)}")
            exploded.add(cloud_id)
            for connection in connections_map.get(cloud_id, []):
                map_next_impulse[connection] = map_next_impulse.get(connection, [])
                map_next_impulse[connection].append(10)

        #logger.debug(f"Stage {stage}: map_next_impulse: {map_next_impulse} energy_map: {energy_map}")
        map_current_impulse = map_next_impulse
        map_next_impulse = {}
        stage += 1
    return exploded


def get_total_energy_excluding_exploded_clouds(energy_map, exploded):

    total_energy = 0
    for cloud_id, energy in energy_map.items():
        if cloud_id not in exploded:
            total_energy += energy
    return total_energy
    
import copy

def calculate_total_energy(initial_energy_map, connections_map, cloud_id, initial_energy, limit):
    energy_map = copy.deepcopy(initial_energy_map)
    exploded = disperse_energy_with_explosions(energy_map, connections_map, cloud_id, initial_energy, limit)

    logger.debug(f"Start cloud id {cloud_id} energy_map: {energy_map} exploded: {exploded}")
    return get_total_energy_excluding_exploded_clouds(energy_map, exploded)


def solve_part3(filename, limit):
    text = file_helper.get_text(filename)
    #logger.debug(f"Text: {text}")
    initial_energy = 10
    initial_energy_map, connections_map = common.get_cloud_maps(text)
    
    total_energy_set = set()
    for cloud_id in initial_energy_map.keys(): 
        total_energy_set.add(calculate_total_energy(initial_energy_map, connections_map, cloud_id, initial_energy, limit))
    
    return max(total_energy_set)