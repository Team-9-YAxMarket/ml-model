from typing import List, Optional
from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str = "ok"


class ResponseBase(BaseModel):
    """Response model base class.

    It is forbidden to have fields not provided for by the scheme.
    """
    class Config:
        allow_population_by_field_name = True


class SKUResponse(ResponseBase):
    sku: str
    add_packs: List[Optional[str]]


class RecommendationResponse(ResponseBase):
    status: str = "Ok"
    orderId: str
    package: str
    items: List[Optional[SKUResponse]]
    no_room_for: List[Optional[SKUResponse]]
