""" Populate's Mongo DB from  CSV """

from mongoengine import connect
import pandas as pd
import json

connect('project1', host='192.168.1.35', port=12345, username='webapp', password='pwd123', authentication_source='admin')

#Loads data from CSV into a dataframe
frame = pd.read_csv('support/movie_metadata.csv', encoding = 'ISO-8859-1')
frame.to_json('movie_data.json')                             
frame = open('movie_data.json').read()                       
data = json.loads(frame)  

print(data)

