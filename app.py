from fastapi import FastAPI, Query, Path
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

# Try to create a 'students' collection within the selected database
try:
    # Creating a collection named 'students' within the selected database
    collection = client["students"]

    # Printing a message indicating a successful collection creation
    print("Collection 'students' created successfully")

except Exception as e:
    # Handling exceptions and printing an error message if collection creation fails
    print(f"Error: {e}")

@app.get('/products')
def list_products(
    min_price: float = Query(default=None, description="minimum price"),
    max_price: float = Query(default=None, description="maximum price")
):
    products = []
    return {"data": list(products)}


@app.post('/purchase-order/create', status_code=201)
def create_course(model: None):
    return


