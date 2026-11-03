from helpers import logging_helper, file_helper

logger = logging_helper.get_logger_instance()


def disperse_energy(energy_map, connections_map, cloud_id, energy_value):
    if energy_value <= 0:
        return
    
    energy_map[cloud_id] = energy_map.get(cloud_id, 0) + energy_value
    for connection in connections_map[cloud_id]:
        disperse_energy(energy_map, connections_map, connection, energy_value -1)


def solve_part2(filename):
    text = file_helper.get_text(filename)
    logger.debug(f"Text: {text}")

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

    start_id = -1
    connection_count = 0
    for id, connections in connections_map.items():
        if len(connections) > connection_count:
            connection_count = len(connections)
            start_id = id
    logger.debug(f"Start ID: {start_id}, Connection Count: {connection_count}")


    initial_energy = 10
    disperse_energy(energy_map, connections_map, start_id, initial_energy)

    logger.debug(f"Energy Map: {energy_map}")

    ans = 0
    for energy in energy_map.values():
        ans += energy
    return ans