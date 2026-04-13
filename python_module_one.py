from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
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
        PASS = 'userpassword835'
        HOST = '.com'
        PORT = 31544
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
# A method that inserts a document into a specified MongoDB database and collection
    def create(self, data):
        # Check to see if data exists
        if data:
            # If there is a list, more than one document, then insert_many
            if isinstance(data, list):
                # Insert many documents and assign it to result
                result = self.database.animals.insert_many(data)
                # Return whether documents were inserted or not
                return bool(result.inserted_ids)
            # Else there is only one document, so insert_one document
            else:
                # Insert one document and assign it to result
                result = self.database.animals.insert_one(data) 
                # Return whether document was inserted or not
                return bool(result.inserted_id)
        else:
            # If data is not available then nothing to insert
            raise Exception("Nothing to create, because data parameter is empty")

# Create method to implement the R in CRUD.
# A method that queries for documents from a specified MongoDB database and collection
    def read(self, data):
        # Check to see if data exists
        if data:
            # Find documents, and assign all the results into a list
            result = list(self.database.animals.find(data))  
            # Returns the list of results
            return result
        else:
            # If data is not available then nothing to return
            return []
            raise Exception("Nothing to read, because data parameter is empty")

# Create method to implement the U in CRUD.
# A method that queries for and changes document(s) from a specified MongoDB database and collection
    def update(self, data, update_data):
        # Check to see if data and the updates requested exist
        if data and update_data:
            # If there is a list, more than one document, then update_many 
            if isinstance(data, dict):  
                # Update multiple documents and assign it to result
                result = self.database.animals.update_many(
                    data, {'$set': update_data}
                )
                # Return the number of modified documents
                return result.modified_count
            # Else there is only one document, so update_one document
            else:  
                # Update one document and assign it to result
                result = self.database.animals.update_one(
                    data, {'$set': update_data}
                )
                # Return the number of modified documents
                return result.modified_count
        else:
            # If data is not available then nothing to update
            raise Exception("Nothing to update, because data parameter is empty")
            
# Create method to implement the D in CRUD.
# A method that queries for and removes document(s) from a specified MongoDB database and collection
    def delete(self, data):
        # Check to see if data exists
        if data:
            # If there is a list, more than one document, then delete_many
            if isinstance(data, dict):  
                # Delete multiple documents and assign it to result
                result = self.database.animals.delete_many(data)   
                # Return the number of deleted documents
                return result.deleted_count
            # Else there is only one document, so delete_one document
            else: 
                # Delete one document and assign it to result
                result = self.database.animals.delete_one(
                data  # Single filter for matching document
                )   
                # Return the number of deleted documents
                return result.deleted_count
        else:
            # If data is not available then nothing to delete
            raise Exception("Nothing to delete, because data parameter is empty")

        