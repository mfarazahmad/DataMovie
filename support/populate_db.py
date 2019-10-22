""" Populate's Mongo DB from  CSV """

from pymongo import MongoClient
import pandas as pd
import json

client = MongoClient('example.com', username='user', password='password', authSource='the_database', authMechanism='SCRAM-SHA-256')

#Loads data from CSV into a dataframe
frame = pd.read_csv('support/movie_metadata.csv', encoding = 'ISO-8859-1')
frame.to_json('movie_data.json')                             
frame = open('movie_data.json').read()                       
data = json.loads(frame)  

print(data)


