from movies import movies

def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie.get('category') == category]
    total_score = sum(movie.get('imdb', 0) for movie in category_movies)
    num_movies = len(category_movies)

    if num_movies > 0:
        return total_score / num_movies
    else:
        return 0

category = input("Enter a category: ")
avg_score = average_imdb_score_by_category(movies, category)
print(f"Average IMDB score for {category} movies:", avg_score)
