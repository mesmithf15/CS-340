from pymongo import MongoClient
from bson.objectid import ObjectId
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32327
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Creates and inserts data given by user into animal collection database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Reads data inputted by user and returns true if passing else false
    def read(self, data):
        if data:
           _data = self.database.animals.find(data, {'_id' : 0})
           
        else:
            _data = self.database.animals.find({}, {'_id' : 0})
        
        return _data

# Update Method used to take data in animals collection and using key to determine what
# needs to be updated and replaces it with value given by user.
    def update(self, data, update_key, update_value):
    	if update_key is not None:
    	    result = self.database.animals.update_one(data, {'$set':{update_key: update_value}})
    	    # Return's the updated change
    	    return result.raw_result
    	else:
    	    raise Exception("Data not found in animal database")

# Delete Method
    def delete(self, data):
    	if data is not None:
    	    result = self.database.animals.delete_many(data)
    	    return result.raw_result
    	else:
    	    raise Exception("Could not delete data from database")
