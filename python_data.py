from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password):
        try:
            self.client = MongoClient('mongodb://localhost:27017')
            self.database = self.client['AAC']
            self.collection = self.database['animals']
            # Add indexes on commonly queried columns
            self.collection.create_index('Breed')
            self.collection.create_index('Animal Type')
            self.collection.create_index('Outcome Type')
        except Exception as e:
            raise Exception(f'Failed to connect to the database, reason: {e}')

# Complete this create method to implement the C in CRUD.
# A method that inserts a document into a specified MongoDB database and collection
    def create(self, data):
        try:
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
        except Exception as e:
            raise Exception('Create has failed, reason: {e}')

# Create method to implement the R in CRUD.
# A method that queries for documents from a specified MongoDB database and collection
    def read(self, data=None):
        try:
            # Check to see if data exists
            if data is None:

                data = {}
            # Find documents, and assign all the results into a list
            result = list(self.database.animals.find(data))  
            # Returns the list of results
            # Return list of results
            return result
        except Exception as e:
            raise Exception('Read has failed, reason: {e}')

# Create method to implement the U in CRUD.
# A method that queries for and changes document(s) from a specified MongoDB database and collection
    def update(self, data, update_data):
        try:
            # Check to see if data and the updates requested exist
            if data and update_data:
                # If there is a list, more than one document, then update_many 
                if isinstance(data, dict) and len(data) > 1:
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
        except Exception as e:
            raise Exception('Update has failed, reason: {e}')
                
# Create method to implement the D in CRUD.
# A method that queries for and removes document(s) from a specified MongoDB database and collection
    def delete(self, data):
        try:
            # Check to see if data exists
            if data:
                # If there is a list, more than one document, then delete_many
                if isinstance(data, dict) and len(data) > 1:
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
        except Exception as e:
            raise Exception('Delete has failed, reason: {e}')

        