from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the animals collection, and the aac user.
        # Definitions of the connection string variables are unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Messenger2'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:30169/test?authSource=AAC' % ("aacuser","Messenger2"))
        self.database = self.client['AAC']
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary   
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    # Complete this create method to implement the R in CRUD.
    def read(self, searchData=0):
        if searchData != 0:
            data = self.database.animals.find(searchData, {"_id": False})
            #for document in data :
                #print(document)
        else:
            data = "Not found."
        return data
            
    # Complete this create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        if updateData is not None:
            if self.database.animals.count_documents(searchData, limit = 1) != 0:
                newResult = self.database.animals.update_many(searchData, {"$set": updateData})
                result = newResult.raw_result           
            else:
                result = "Not found."
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty.")
            
    # Complete this create method to implement the U in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            if self.database.animals.count_documents(deleteData, limit = 1) != 0:
                deletedResult = self.database.animals.delete_many(deleteData)
                result = deletedResult.raw_result   
            else:
                result = "Not found."
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty.")
            