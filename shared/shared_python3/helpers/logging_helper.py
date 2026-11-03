import logging
import logging.config

def get_logger_instance():
    """
    Create and return a logger instance (using the configuration from 'logging.conf').
    """
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger = logging.getLogger('simpleLogger')
    return logger