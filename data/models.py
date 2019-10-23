import os, json
from mongoengine import *

#hostname = os.environ.get("hostname")
#user_id = os.environ.get("user_id")
#user_pass = os.environ.get("user_pass")

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


class Actor():
    
    def __init__(self, name):
        self.name = name
        self.movies = []
        self.genres = []
        self.facebook_likes = 0
        self.highest_profit = {"movie": "", "profit":0}

    def ActorData(self):
        profits = [0]

        movie_data = movie_stats.objects(Q(actor_1_name=self.name) | Q(actor_2_name=self.name) | Q(actor_3_name=self.name))
           
        for movie in movie_data:
            self.movies.append(movie.movie_title.replace(u'\xa0',u'').replace('Â ', ''))
            self.genres.append(movie.genres.replace(u'\xa0',u'').replace('Â ', ''))

            if self.name == movie.actor_1_name:
                self.facebook_likes = movie.actor_1_facebook_likes
            elif self.name == movie.actor_2_name:
                self.facebook_likes = movie.actor_2_facebook_likes
            elif self.name == movie.actor_3_name:
                self.facebook_likes = movie.actor_3_facebook_likes

            if movie.gross and movie.budget:
                profits.append((movie.gross - movie.budget)/movie.budget)
                if max(profits) > self.highest_profit['profit']:
                    self.highest_profit = {"movie": movie.movie_title, "profit":max(profits)}

def MovieData():
    profits = [0]
    max_profits = {"movie": "", "profit":0}

    movie_data = movie_stats.objects()

    for movie in movie_data:
        if movie.gross and movie.budget:
            profits.append((movie.gross - movie.budget)/movie.budget)
            if max(profits) > max_profits['profit']:
                max_profits.update({"movie": movie.movie_title, "profit":max(profits)})

                if 'Paranormal' in movie.movie_title:
                    print(movie.gross, flush=True)
                    print(movie.budget, flush=True)
    
    return max_profits

most_profitable = MovieData()
print(most_profitable, flush=True)