from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):

        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # CREATE
    def create(self, data):

        if data is not None:
            try:
                self.database.animals.insert_one(data)
                return True
            except Exception as e:
                print("Create error:", e)
                return False
        else:
            raise Exception("Nothing to save, data parameter is empty")

    # READ
    def read(self, query):

        if query is not None:
            try:
                data = self.database.animals.find(query)
                return list(data)
            except Exception as e:
                print("Read error:", e)
                return []
        else:
            return []

    # UPDATE
    def update(self, query, new_values):

        if query is not None and new_values is not None:
            try:
                result = self.database.animals.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print("Update error:", e)
                return 0
        else:
            raise Exception("Missing query or update data")

    # DELETE
    def delete(self, query):

        if query is not None:
            try:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0
        else:
            raise Exception("Missing query parameter")