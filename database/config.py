from pymongo import MongoClient

client = MongoClient("mongodb://root:root@localhost:27017/cosmiccloud?retryWrites=true&w=majority&connectTimeoutMS=1000")
db = client.cosmiccloud
product_catalogue_collection = db["product_catalogue"]
purchase_orders_collection = db["purchase_orders"]


