from decimal import Decimal
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, PositiveInt


class HealthCheckResponse(BaseModel):
    status: str = "ok"


class SKUResponse(BaseModel):
    sku: Optional[str]
    count: Optional[PositiveInt]
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    weight: Optional[Decimal]
    cargotypes: Optional[List[str]]
    img: Optional[AnyUrl]
    barcode: Optional[str]


class PredictResponse(BaseModel):
    orderId: Optional[str]
    package: str
    items: List[SKUResponse]
