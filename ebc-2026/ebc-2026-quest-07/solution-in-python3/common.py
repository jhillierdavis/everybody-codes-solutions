from helpers import logging_helper

logger = logging_helper.get_logger_instance()

def disperse_energy(energy_map, connections_map, cloud_id, energy_value):
    if energy_value <= 0:
        return
    
    energy_map[cloud_id] = energy_map.get(cloud_id, 0) + energy_value
    for connection in connections_map[cloud_id]:
        disperse_energy(energy_map, connections_map, connection, energy_value -1)


def get_cloud_maps(text):
    energy_map = {}
    connections_map = {}

    for line in text.splitlines():
        logger.debug(f"Processing line: {line}")    
        entries = line.strip().split()
        id = int(entries[0].split("=")[1].strip(','))
        energy = int(entries[1].split("=")[1].strip(','))
        connections = [int(x) for x in entries[2].split("=")[1].split(',')]

        logger.debug(f"ID: {id}, Energy: {energy}, Connections: {connections}")
        energy_map[id] = energy
        connections_map[id] = connections       

    return energy_map, connections_map


def get_cloud_start_id(connections_map):
    start_id = -1
    connection_count = 0
    for id, connections in connections_map.items():
        if len(connections) > connection_count:
            connection_count = len(connections)
            start_id = id
    logger.debug(f"Start ID: {start_id}, Connection Count: {connection_count}")    
    return start_id


def get_total_energy_of_all_clouds(energy_map):
    total_energy = 0
    for energy in energy_map.values():
        total_energy += energy
    return total_energy