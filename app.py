from fastapi import FastAPI
from routes.route import router
import motor.motor_asyncio
import sys

MONGODB_URL = "mongodb://root:root@localhost:27017/cosmiccloud?retryWrites=true&w=majority&connectTimeoutMS=1000"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

product_catalogue_collection = client.get_database().get_collection('product_catalogue')
purchase_order_collection = client.get_database().get_collection('purchase_orders')

# FastAPI event loop starts here
app = FastAPI(
    title="CosmoCloud WA",
    summary="consists of two APIs - get list of available products to show as a catalogue, post an order for an item from UI.."
)

try:
    # Send a ping to confirm a successful connection
    client.server_info()
    print("Pinged MongoDB. Successfully connected!")
except Exception as e:
    print(f"Connection error: {e}")
    sys.exit("MongoDB connection failed. Shutting down...")

app.include_router(router)



