from pydantic import BaseModel


class PredictResponse(BaseModel):
    orderId: str
    package: str
    status: str