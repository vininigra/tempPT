from core.services.ConnectionService import ConnectionService


class MongoService:
    def __init__(self, conection: ConnectionService, dbname) -> None:
        self.client = conection.getConnection
        self.db = self.client[dbname]

    def insert(self, collection, **kwargs):
        data = {}
        collection = self.db[collection]
        for key, value in kwargs.items():
            data[key] = value

        collection.insert_one(data)

    def find(self, collection, **kwargs):
        collection = self.db[collection]
        return collection.find(kwargs)

    def findOne(self, collection, **kwargs):
        collection = self.db[collection]
        return collection.find_one(kwargs)

    def delete(self, collection, **kwargs):
        collection = self.db[collection]
        collection.delete_one(kwargs)

    def update(self, collection, **kwargs):
        collection = self.db[collection]
        collection.update_one(kwargs)
