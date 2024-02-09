from movies import movies

def filter_movies_above_average(movies):
    return [movie for movie in movies if movie.get('imdb', 0) > 5.5]

filtered_movies = filter_movies_above_average(movies)
print(filtered_movies)
