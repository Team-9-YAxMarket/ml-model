from decimal import Decimal
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field, NonNegativeInt, condecimal


class RequestBase(BaseModel):
    """Request model base class.

    It is forbidden to have fields not provided for by the scheme."""

    class Config:
        extra = Extra.forbid


# class SKURequest(RequestBase):
#     """SKU request model."""
#
#     sku: str
#     size_1: condecimal(gt=Decimal(0)) = Field(..., alias="size1")
#     size_2: condecimal(gt=Decimal(0)) = Field(..., alias="size2")
#     size_3: condecimal(gt=Decimal(0)) = Field(..., alias="size3")
#     weight: condecimal(gt=Decimal(0))
#     sku_type: list[NonNegativeInt] = Field(..., alias="type")
#
#
# class OrderRequest(RequestBase):
#     """Order request model."""
#
#     order_id: UUID = Field(..., alias="orderId")
#     items: list[SKURequest]
#
#
# class CartonAmountRequest(RequestBase):
#     """Carton leftovers in the warehouse request model."""
#
#     carton_type: str
#     amount: NonNegativeInt
#
#
# class FullInfoRequest(RequestBase):
#     """Full info request model."""
#
#     order: OrderRequest
#     carton_leftovers: list[CartonAmountRequest]

class SKU(RequestBase):
    sku: Optional[str]
    barcode: Optional[str]
    img: Optional[str]
    count: Optional[int]
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    weight: Optional[Decimal]
    cargotypes: Optional[List[str]]


class Order(RequestBase):
    orderId: Optional[str]
    package: Optional[str] = ""
    status: Optional[str] = ""
    items: List[SKU]
