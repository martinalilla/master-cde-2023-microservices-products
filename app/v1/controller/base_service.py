import logging
from v1.config import Settings, get_config
from fastapi import Depends

# This service contains the business logic.
# This is extended by other services in order to allow code reusing without duplicate it.

_config: Settings = get_config()

class BaseService:

    def __init__(
            self,
            config: Settings = Depends(get_config)
    ):
        self.config: Settings = config 
        self.logger: logging.Logger = logging.getLogger(_config.service_name)
