from data.models import movie_stats, connectToDB
from data.actor import Actor

connectToDB()       #Intialize DB

def topTenGenres():
    """ This method is used to calculate the top ten genres and return it in order of decreasing profitablity. """
    genres = set()
    movie_data = movie_stats.objects()
    for movie in movie_data:
        genre_list = movie.genres.split('|')
        for genre in genre_list:
            genres.add(str(genre))

    if (movie_data):
        genre_stats = []
        for genre in genres:
                genre_profits = {"genre":"", "profit":0}
                genre_data = movie_stats.objects(genres__contains=genre)
                for movie in genre_data:
                    if movie.gross and movie.budget:
                        genre_profits['genre'] = genre
                        genre_profits['profit'] += (movie.gross - movie.budget)
                genre_stats.append(genre_profits)
    
    genre_stats.sort(key=lambda x: x['profit'], reverse=True)
    genre_stats = genre_stats[0:9]
    return genre_stats

def topTenDirectors():
    """ This method is used to calculate the top ten directors and return it in order of decreasing profitablity. """
    director_names = set()
    movie_data = movie_stats.objects()
    for movie in movie_data:
        if movie.gross and movie.budget:
            director_names.add(str(movie.director_name))

    if (movie_data):
        dir_stats = []
        for director in director_names:
                dir_profits = {"name":"", "profit":0}
                director_data = movie_stats.objects(director_name__=director)
                for movie in director_data:
                    if movie.gross and movie.budget:
                        dir_profits['name'] = director
                        dir_profits['profit'] += (movie.gross - movie.budget)
                dir_stats.append(dir_profits)
    
    dir_stats.sort(key=lambda x: x['profit'], reverse=True)
    dir_stats = dir_stats[0:9]
    return dir_stats

def actorList():
    """ This method is used to find all the actors available. """
    actor_names = set()
    movie_data = movie_stats.objects()
    for movie in movie_data:
        if movie.actor_1_name:
            actor_names.add(movie.actor_1_name)
        if movie.actor_2_name:
            actor_names.add(movie.actor_2_name)
        if movie.actor_3_name:
            actor_names.add(movie.actor_3_name)

    actor_names = sorted(list(actor_names))
    return list(actor_names)

def actorStats(actorname):
    """ This method is used to find a specific actor's information """
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