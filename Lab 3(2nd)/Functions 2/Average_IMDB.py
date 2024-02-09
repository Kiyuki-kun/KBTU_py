from movies import movies

def average_imdb_score(movies):
    total_score = sum(movie.get('imdb', 0) for movie in movies)
    num_movies = len(movies)
    if num_movies > 0:
        return total_score / num_movies
    else:
        return 0

avg_score = average_imdb_score(movies)
print("Average IMDB score:", avg_score)
