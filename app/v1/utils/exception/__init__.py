
from functools import lru_cache
import logging
from typing import Any, Dict, Optional
from fastapi import FastAPI, HTTPException, Request, Response
import requests
from starlette import status
import sys
import traceback

from v1.config.config import Settings, get_config


_config: Settings = get_config()


class HttpCustomException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None,
            internal_detail: str = None,
            error_code: Optional[str] = None,
            headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)
        self.internal_detail = internal_detail
        self.headers = headers
        self.error_code = error_code
        logger = logging.getLogger(_config.service_name)
        logger.exception(f"{status_code} : {detail}", exc_info=False, stack_info=False)
        logger.debug({traceback.format_exc()})



class CustomExceptionHandler:
    def __init__(self, logger_name: str):
        self.logger_name = logger_name
        if _config.env != "local":
            sys.tracebacklimit = 1
    

    def handle_custom_exception(self, msg: Optional[str] = ""):
        logger = logging.getLogger(self.logger_name)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        logger.exception(f"{status_code} : {msg}", exc_info=False, stack_info=False)
        logger.debug({traceback.format_exc()})

        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=msg,
            )
    

async def handle_generic_exception(request: Request, call_next):
    try:
        return await call_next(request)
    except requests.exceptions.HTTPError as e:
        return e.response
    except HttpCustomException:
        raise
    except Exception as e:
        logger = logging.getLogger(_config.service_name)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        logger.exception(f"{request.method} {request.url} {status_code} : {repr(e)}", exc_info=False, stack_info=False)
        logger.debug({traceback.format_exc()})
        return Response(content="A generic problem occured", status_code=500)
    

@lru_cache()
def custom_exception_handler() -> CustomExceptionHandler:
    return CustomExceptionHandler(_config.service_name)