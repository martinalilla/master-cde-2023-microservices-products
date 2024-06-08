from typing import Optional

from pydantic import BaseModel
from v1.router.endpoint_responses import get_all_responses, delete_all_responses, post_responses

class Schema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    example: Optional[dict | list] = None

    class Config:
        frozen = True

class APIMetadata(BaseModel):
    summary: str
    description: str
    operationId: str
    responses: dict
    input: Optional[Schema] = None
    output: Optional[Schema] = None

    class Config:
        frozen = True

CREATE_PRODUCT = APIMetadata(
    summary="Create a new product",
    description="Creates a new product in the system",
    operationId="CREATE_PRODUCT",
    responses=post_responses, 
    input=Schema(
        title="Product Input",
        description="The product content",
    example={
            "name": "Amazing T-Shirt",
            "description": "This is a high-quality, comfortable T-Shirt",
            "category_id": "7e96755c-88a3-4f3d-9f59-4d3ab3b277ee",
            "brand_id": "1c1a8ef9-7dab-4397-b73a-5f9a4143c135",
            "price": 19.99,
            "weight": 0.25,
    }
    ),
    output=Schema(
        title="Product Created",
        description="The newly created product information",
        example={
            "product_id": "1caff255-ef44-4066-a7a3-884c81c34ecf",
            "created_at": "2024-06-08T17:40:00Z",
        },
    ),
)