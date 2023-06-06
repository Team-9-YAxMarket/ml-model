from uuid import UUID

from pydantic import BaseModel, Field, PositiveInt


class HealthCheckResponse(BaseModel):
    status: str = "ok"


class ResponseBase(BaseModel):
    """Response model base class.

    It is forbidden to have fields not provided for by the scheme."""

    class Config:
        allow_population_by_field_name = True


class SKUResponse(ResponseBase):
    sku: str
    amount: PositiveInt


class PackResponse(ResponseBase):
    packages: list[str]
    items: list[SKUResponse]


class RecommendationResponse(ResponseBase):
    order_id: UUID = Field(..., alias="orderId")
    packs: list[PackResponse]
    status: str = "Ok"
