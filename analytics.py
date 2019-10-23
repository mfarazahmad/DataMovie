import pandas
from data.models import Actor

def topTenGenres():
    """ This method is used to calculate the top ten genres and return it in order of decreasing profitablity. """
    topGenres = []

    return topGenres

def topTenActors():
    """ This method is used to calculate the top ten actors and return it in order of decreasing profitablity. """
    topGenres = []
    return topGenres

def topTenDirectors():
    """ This method is used to calculate the top ten directors and return it in order of decreasing profitablity. """
    topGenres = []
    return topGenres

def actorList():
    actors = []
    return actors

def actorStats(actorname):
    actor = Actor(actorname)
    actor.ActorData()

    actor_name = actor.name
    highest_profit = actor.highest_profit
    facebook_likes = actor.facebook_likes
    genres = actor.genres
    movies = actor.movies

    stats = {"actor_name":actor_name , "facebook_likes":facebook_likes, "highest_profit":highest_profit, 
            "genres":genres, "movies":movies}

    return stats