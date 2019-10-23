import os, json
from mongoengine import *
from .models import movie_stats

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
        genres = set()
        for movie in movie_data:
            self.movies.append(movie.movie_title.replace(u'\xa0',u'').replace('Â ', ''))
            
            genre_list = movie.genres.split('|')
            for genre in genre_list:
                genres.add(str(genre).replace(u'\xa0',u'').replace('Â ', ''))

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
        self.genres.append(list(genres))