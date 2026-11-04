from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()

import common


def disperse_energy_with_explosions(energy_map, connections_map, cloud_id, energy_value, limit):
    """
    Disperse energy through the cloud network, handling explosions.

    Parameters:
    - energy_map: Dictionary mapping cloud_id to its current energy.
    - connections_map: Dictionary mapping cloud_id to a list of connected cloud_ids.
    - cloud_id: The starting cloud_id for energy dispersion.
    - energy_value: The initial energy to disperse.
    - limit: The energy threshold for a cloud to explode.

    Returns:
    - A set of cloud_ids that have exploded.
    """

    exploded = set()   
    stage = 1

    current_impulse_map = {} # Holds the current stage's impulses for each cloud
    next_impulse_map = {} # Holds the next stage's impulses for each cloud
    
    current_impulse_map[cloud_id] = {energy_value:1}

    while current_impulse_map:
        if stage > 100:  # Prevent infinite loops
            logger.warning(f"Stage {stage}: Exceeded maximum stages, stopping to prevent infinite loop.")
            return exploded
        
        for cloud_id, impulse_map in current_impulse_map.items():
            if cloud_id in exploded:
                continue

            for value, multiplier in impulse_map.items():
                next_energy_value =  energy_map.get(cloud_id, 0) + (value * multiplier)
                energy_map[cloud_id] = next_energy_value

            for connection in connections_map.get(cloud_id, []):   
                for value, multiplier in impulse_map.items():
                    new_value = value - 1 # Increment multiple for new value    
                    if (new_value <= 0):
                        continue

                    if not next_impulse_map.get(connection):
                        next_impulse_map[connection] = {}

                    map_ref = next_impulse_map.get(connection, {}) # Reference to the impulse map for this connection (holding a value & its multiplier)
                    current_multiplier =  map_ref.get(new_value, 0)
                    next_impulse_map[connection][new_value] = current_multiplier + multiplier

            handle_explosions(energy_map, connections_map, exploded, next_impulse_map, limit)

        #logger.debug(f"Stage {stage}: next_impulse_map: {next_impulse_map} energy_map: {energy_map}")
        current_impulse_map = next_impulse_map
        next_impulse_map = {}
        stage += 1
    return exploded


def handle_explosions(energy_map, connections_map, exploded, map_next_impulse, limit):
        explosion_pulse_value = 10
        for cloud_id in energy_map.keys():
            if cloud_id in exploded:
                continue

            current_energy = energy_map.get(cloud_id, 0)
            if current_energy < limit:
                continue

            #logger.debug(f"Stage {stage}: Cloud {cloud_id} exploded with energy {energy_map.get(cloud_id, 0)}")
            exploded.add(cloud_id)
            for connection in connections_map.get(cloud_id, []):
                map_next_impulse[connection] = map_next_impulse.get(connection, {})
                map_ref = map_next_impulse[connection] # Reference to the impulse map for this connection (holding a value & its multiplier)

                current_multiplier =  map_ref.get(explosion_pulse_value, 0)                                   
                map_ref[explosion_pulse_value] = current_multiplier + 1    


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