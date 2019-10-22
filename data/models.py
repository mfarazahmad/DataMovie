import pymongo
import os

hostname = os.environ.get("hostname")
user_id = os.environ.get("user_id")
user_pass = os.environ.get("user_pass")

class Actor():

    def __init__(self, name):
        self.name = name
        self.likes = 0
        self.grossing_movie = ""
        self.recognized_for = ""
        self.top_genre = ""

    def calculate_likes():

    def calculate
