from scrape import scrape
import json

try :
    recipes_list = scrape('recipe/26670/taylors-piroshki/', 5)
    with open('recipes.json', 'w') as f:
        json.dump(recipes_list, f)
except Exception as e:
    print(e)

"""when the ingrediants are turned into json the unicode of
the string is modified, to handle this problem, you may utilize the functions
below : 
    import unicodedata

    s = '1¼ cups graham cracker crumbs'
    s_normalized = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')

    print(s_normalized) # Output: "1 1/4 cups graham cracker crumbs"

"""