def CategoryList(category): 
  
    category_list = [movie["name"] for movie in ('movies') if movie["category"] == category]
    return category_list 
CategoryList("Romance")
['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']
