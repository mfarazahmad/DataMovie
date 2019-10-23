import os, json
from mongoengine import *

#hostname = os.environ.get("hostname")
#user_id = os.environ.get("user_id")
#user_pass = os.environ.get("user_pass")

def connectToDB():
    connect('movie_db', host='localhost', port=27017)

class movie_stats(Document):
    movie_title = StringField()

    director_name = StringField()
    actor_1_name = StringField()
    actor_1_facebook_likes = StringField()
    actor_2_name = StringField()
    actor_2_facebook_likes = StringField()
    actor_3_name = StringField()
    actor_3_facebook_likes = StringField()

    budget = IntField()
    gross = IntField()
    movie_facebook_likes = IntField()
    genres = StringField()
    plot_keywords = StringField()

    num_user_for_reviews = IntField()
    num_critic_for_reviews = IntField()
    num_voted_users = IntField()
    imdb_score = IntField()

    title_year = IntField()
    country = StringField()
    duration = IntField()
    cast_total_facebook_likes = IntField()
    director_facebook_likes = IntField()
    facenumber_in_poster = IntField()
    color = StringField()
    aspect_ratio = StringField()
    language = IntField()
    content_rating = StringField()
    movie_imdb_link = StringField()