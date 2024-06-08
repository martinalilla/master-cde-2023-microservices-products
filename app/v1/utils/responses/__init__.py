from pydantic import BaseModel


class StatusResponse(BaseModel):
    content: dict
    description: str


HTTP_200_OK: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Success"
)

HTTP_201_CREATED: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Object Created"
)

HTTP_202_ACCEPTED: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Object updated"
)

HTTP_400_BAD_REQUEST: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="The server cannot or will not process the request due to something that is perceived to be a client error"
)

HTTP_401_UNAUTHORIZED: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Unauthorized. Ensure you are using a valid JWT token.",
)

HTTP_403_FORBIDDEN: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Credential error. Ensure you are using a valid JWT token.",
)

HTTP_422_UNPROCESSABLE_ENTITY: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Check parameter values correctness in according to the documentation above.",
)

HTTP_500_INTERNAL_SERVER_ERROR: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Internal server error. Please contact the support team.",
)

HTTP_503_SERVICE_UNAVAILABLE: StatusResponse = StatusResponse(
    content={"application/json": {}},
    description="Service is not currently available. Try again later or contact the support team.",
)