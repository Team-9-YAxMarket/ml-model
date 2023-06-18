from decimal import Decimal
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Extra, PositiveInt


class RequestBase(BaseModel):
    """Request model base class.

    It is forbidden to have fields not provided for by the scheme."""

    class Config:
        extra = Extra.ignore


class SKU(RequestBase):
    sku: Optional[str]
    count: Optional[PositiveInt]
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    weight: Optional[Decimal]
    cargotypes: Optional[List[str]]
    img: Optional[AnyUrl]
    barcode: Optional[str]


class Order(RequestBase):
    orderId: Optional[str]
    package: Optional[str] = ""
    items: List[SKU]
