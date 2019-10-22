import pandas
from .data.actor import Actor

def topTenGenres():
"""" This method is used to calculate the top ten genres and return it in order of decreasing profitablity. """"
    topGenres = []
    return topGenres

def topTenActors():
"""" This method is used to calculate the top ten actors and return it in order of decreasing profitablity. """"
    topGenres = []
    return topGenres

def topTenDirectors():
"""" This method is used to calculate the top ten directors and return it in order of decreasing profitablity. """"
    topGenres = []
    return topGenres

def actorStats(actorname):
    actor = Actor(actorname)

    actor_name = actor.name
    facebook_likes = actor.likes
    highest_grossing_movie = actor.grossing_movie
    most_known_movie = actor.recognized_for
    most_known_for_genre = actor.top_genre

    stats = {"actor_name":actor_name , "facebook_likes":facebook_likes, "highest_grossing_movie":highest_grossing_movie, 
            "most_known_movie":most_known_movie, "most_known_for_genre":most_known_for_genre}

    return stats