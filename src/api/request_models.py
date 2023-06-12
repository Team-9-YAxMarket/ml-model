from decimal import Decimal

from pydantic import BaseModel, Extra


class RequestBase(BaseModel):
    """Request model base class.

    It is forbidden to have fields not provided for by the scheme."""

    class Config:
        extra = Extra.forbid


class SKURequest(RequestBase):
    """SKU request model."""

    sku: str
    count: int
    size1: Decimal
    size2: Decimal
    size3: Decimal
    weight: Decimal
    type: list[int]


class OrderRequest(RequestBase):
    """Order request model."""

    orderId: str
    items: list[SKURequest]
