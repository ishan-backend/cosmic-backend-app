import motor.motor_asyncio
from fastapi import FastAPI

app = FastAPI()

uri = "mongodb://root:root@localhost:27017/admin"
# Create a new client and connect to the server
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

MONGODB_URL="mongodb+srv://root:root@localhost:27017/admin?retryWrites=true&w=majority"
client2 = motor.motor_asyncio.AsyncIOMotorClient("MONGODB_URL")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    client2.admin.command('ping')
    print("Pinged your deployment. You have successfully connected to MongoDB!")
except Exception as e:
    print(e)