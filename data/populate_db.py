""" Populate's Mongo DB from  CSV """
from pymongo import MongoClient
import pandas as pd
import json

def populate_csv():
    #Connects to MongoDBs
    cursor = MongoClient('localhost', 27017)
    db = cursor["movie_db"]
    collection = db["movie_stats"]

    #Loads data from CSV into a dataframe
    frame = pd.read_csv('support/movie_metadata.csv', encoding = 'ISO-8859-1')                   
    data = json.loads(frame.to_json(orient='records'))  
    print(data)

    db_response = collection.insert_many(data)
    print(db_response)

if __name__ == ("__main__"):
    populate_csv()
