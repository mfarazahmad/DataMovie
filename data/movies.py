from .models import *
from mongoengine import *

class Movie(Document):
    actor1 = DictField()
    actor2 = DictField()
    actor3 = DictField()
    director = StringField()
    bugdet = IntField()
    gross = IntField()
    fb_likes = IntField()
    genres = ListField()

class Alt_Movie(Document):
    
    def __init__(self):
        self.actor1 = ""
        self.actor2 = ""
        self.actor3 = ""
        self.director = ""
        self.bugdet = ""
        self.gross = ""
        self.genres = ""
        self.fb_likes = ""

    def calculate_likes():
        pass