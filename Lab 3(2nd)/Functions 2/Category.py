from movies import movies

def filter_movies_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category]

category = input("Enter a categry: ")
filtered_movies = filter_movies_by_category(movies,category)
print(filtered_movies)
