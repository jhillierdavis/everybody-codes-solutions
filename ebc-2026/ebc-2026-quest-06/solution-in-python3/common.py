from helpers import logging_helper

logger = logging_helper.get_logger_instance()

def get_ingredients_map(text:str) -> dict:
    """
    Parse the input text to create a mapping of ingredients.

    Args:
        text (str): The input text containing ingredient mappings in the format "key: value1, value2, ...".

    Returns:
        dict: A dictionary mapping each key to a list of its corresponding values.
    """
    ingredients_map = {}
    for line in text.splitlines():
        key, value = line.split(":")
        ingredients_map[key.strip()] = value.strip().split(",")

    logger.debug("Ingredients map: %s", ingredients_map)
    return ingredients_map