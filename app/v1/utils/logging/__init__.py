import logging
import sys
from v1.config.config import Settings, get_config

_config: Settings = get_config()
    

def setup_logging():
    app_logger = logging.getLogger(_config.service_name)

    format_message = '%(levelname)-8s- %(funcName)20s():%(lineno)4s- %(message)s'
    formatter = logging.Formatter(format_message)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    app_logger.setLevel(logging._nameToLevel[_config.LOGGING_LEVEL])

    return app_logger
