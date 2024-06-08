from datetime import datetime

from fastapi import APIRouter, Depends

from v1.config import Settings, get_config

router = APIRouter(
    tags=['health']
)


@router.get("/health/products")
def health_check(config: Settings = Depends(get_config)):
    return {
        "message": "healthy",
        "version": config.version,
        "time": datetime.now()
    }
