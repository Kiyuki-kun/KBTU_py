from movies import movies

def is_above_average_score(movie):
    
    if 'imdb' in movie:
        return movie['imdb'] > 5.5
    else:
        return False


for i in range(len(movies)):
    print(is_above_average_score(movies[i]))

