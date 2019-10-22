""" Populate's Mongo DB from  CSV """

from pymongo import MongoClient
import pandas as pd
import json

def populate_csv():
    #Connects to MongoDB
    cursor = MongoClient("mongodb://localhost:27017/")
    db = cursor["movie_db"]
    collection = db["movie_stats"]

    #Loads data from CSV into a dataframe
    frame = pd.read_csv('support/movie_metadata.csv', encoding = 'ISO-8859-1')
    frame.to_json('movie_data.json')                             
    frame = open('movie_data.json').read()                       
    data = json.loads(frame)  
    print(data)

    db_response = collection.insert_one(data)
    print(db_response)

if __name__ == ("__main__"):
    populate_csv()
