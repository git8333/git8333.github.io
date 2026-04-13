import os
from python_data import AnimalShelter
import pandas as pd

# Credentials, with defaults if needed
username = os.environ.get('AAC_USERNAME', '')
password = os.environ.get('AAC_PASSWORD', '')

# Start the database
shelter = AnimalShelter(username, password)

# Retreive Database 
df = pd.DataFrame.from_records(shelter.read())

# Drop id in Mongo if field found
if '_id' in df.columns:
    df = df.drop('_id', axis=1)

# Sort through animal id
df = df.sort_values(by=['Animal ID'])