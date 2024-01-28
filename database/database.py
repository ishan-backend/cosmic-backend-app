import motor.motor_asyncio


class Database:
    DB = None
    URI = None

    def __init__(self, uri):
        self.URI = uri

    @staticmethod
    def initialise():
        client = (motor.motor_asyncio.AsyncIOMotorClient(Database.URI))
        Database.DB = client['cosmocloud']

    @staticmethod
    def insert(collection, data):
        Database.DB[collection].insert(data)