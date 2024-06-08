import logging
import sys
from fastapi import FastAPI, Request
from v1.router.public import products_public_router

from v1.config import get_config
from v1.router import health
from v1.utils.exception import  handle_generic_exception

from v1.utils.logging import setup_logging

def main():
    config = get_config()
    title = f"{config.env} - {config.service_name}"

    app = FastAPI(title=config.service_name, description=config.description, version=config.short_sha, debug=True)
    
    ##### ----- Logging setup ------ #####
    app_logger = setup_logging()
    ##### ----- ------ ------ #####

    # Routers
    # /
    app.include_router(health.router)

    # /public/v1
    # Routes that must be publicly accessible.
    # Request pointing to these router should pass through a JWT validator before.
    # JWT validator must add a header (config.Settings.public_header) containing the payload with user infos.
    app.include_router(products_public_router.router, prefix=config.api_public_v1_prefix)


    ##### ----- Logging setup ------ #####

    app_logger.debug('App Initialized.')


    ##### ----- Exceptions setup ------ #####
    @app.middleware("http")
    async def handle_exceptions(request: Request, call_next):
        return await handle_generic_exception(request=request, call_next=call_next)
    ##### ----- ----------- ------ #####
    
    return app

app = main()