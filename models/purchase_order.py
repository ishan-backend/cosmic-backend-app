from pydantic import BaseModel


class PurchaseOrder(BaseModel):
    createdBy: int
    createdByName: str
