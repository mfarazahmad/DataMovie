from pymongo import MongoClient
import os

#hostname = os.environ.get("hostname")
#user_id = os.environ.get("user_id")
#user_pass = os.environ.get("user_pass")

def db_access():
    #Connects to MongoDB
    cursor = MongoClient('localhost', 27017)
    db = cursor["movie_db"]
    collection = db["movie_stats"]

    return collection