from pydantic import BaseModel


# pydantic -  validator and our db table which is our product_catalogue collection
class ProductCatalogue(BaseModel):
    productName: str
    isActive: bool
