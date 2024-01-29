from fastapi import APIRouter, Query, Path
from models.product_catalogue import ProductCatalogue
from models.purchase_order import PurchaseOrder
from database.config import product_catalogue_collection, purchase_orders_collection
from schema.schemas import product_catalogue_list_serializer, po_list_serializer
from bson import objectid

router = APIRouter()


# GET product catalogue items list method
@router.get('/products')
async def list_products(
        min_price: float = Query(default=None, description="minimum price"),
        max_price: float = Query(default=None, description="maximum price")
):
    # products = []
    # return {"data": list(products)}
    res = product_catalogue_list_serializer(product_catalogue_collection.find())
    return res


# POST create order method
@router.post('/purchase-order/create/v1')
async def create_po(purchase_order_model: PurchaseOrder):
    purchase_orders_collection.insert_one(dict(purchase_order_model))
    return

@router.get('/purchase-orders-list/v1')
async def list_po():
    res = po_list_serializer(purchase_orders_collection.find())
    return res
