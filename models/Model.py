from config.database import db

class Model:

    collection_name = ''

    @staticmethod
    def all():
        collection = db[Model.collection_name]
        return list(collection.find())


    @staticmethod
    def create(data):
        collection = db[Model.collection_name]
        return collection.insert_one(data)

    @staticmethod
    def find_one(id):
        collection = db[Model.collection_name]
        return collection.find_one(id)