from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional
import os



class Settings(BaseSettings):
    env: str = Field(os.environ.get("ENVIRONMENT"))
    port: int = os.environ.get('PORT', 8080)
    service_name: str = Field(os.environ.get("MICROSERVICE_NAME"))
    short_sha: str = 'local-sha'
    version: str = Field(os.environ.get("VERSION"))
    description: str = Field(os.environ.get("MICROSERVICE_DESCRIPTION"))
    api_public_v1_prefix: str = '/public/v1'
    api_private_prefix: str = '/v1'
    api_key_header: str = "X-Endpoint-API-UserInfo"
    request_id_header: str = "x-request-id"
    open_api_url: str = '/openapi.yaml'
    docs_url: str = '/public/docs'
    redoc_url: str = '/public/redoc'
    service_url: Optional[str] = os.environ.get("SERVICE_URL")

    # Optional
    public_header:  Optional[str] = os.environ.get("X_ENDPOINT_API_USERINFO")
    private_header: Optional[str] = os.environ.get("PRIVATE_USERINFO")

    # AWS Environment variables
    dynamodb_project_id: Optional[str] = os.environ.get("DYNAMODB_PROJECT_ID")
    PROJECT_ID_DEPLOY:  Optional[str] = os.environ.get("PROJECT_ID_DEPLOY")
    PROJECT_ID_MONITORING:  Optional[str] = os.environ.get("PROJECT_ID_MONITORING")
    LOGGING_LEVEL: Optional[str] = os.environ.get('LOGGING_LEVEL')
    TRACE_SAMPLING: Optional[str] = os.environ.get('TRACE_SAMPLING')



@lru_cache()
def get_config() -> Settings:
    return Settings()
