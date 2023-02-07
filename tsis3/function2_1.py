def good_movie(movie_name):
        for m in ('movies'):       
            if m["name"] == movie_name:      
                if m["imdb"] > 5.5:      
                    return "True"  
                else:       
                    return "False"       