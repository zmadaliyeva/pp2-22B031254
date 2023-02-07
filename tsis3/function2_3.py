def movies_category(category):
    movies_category = []
    for m in ('movie'):
        if m["category"] == category:
            movies_category.append(m["name"])
    return movies_category
romance_movies = movies_category("Romance")
print ('romance_movies')
['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']