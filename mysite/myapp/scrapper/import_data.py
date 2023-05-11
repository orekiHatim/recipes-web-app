from .getOrCreate import getOrCreatePersonne, getOrCreateRecette
from .create import *

def importData(data):
    for obj in data:
        titre = obj['heading']
        description = obj['description']
        tag = obj['category']
        recette = getOrCreateRecette(titre, description, tag)
        #If recipe does not exist we will create one
        if recette != None:
            #Create instances of Image
            for ele in obj['images']:
                #print(ele)
                createImage(recette, ele)

            #Create instances of Ingrediant
            ingrediants = []
            for ele in obj['ingrediants']:
                ingrediants.append(ele)
                
            if len(ingrediants) >= 2:
                for ele in ingrediants:
                    keys = list(ele.keys())
                    #print(type(keys))
                    #print(keys)
                    key = keys[0]
                    values = ele[key]
                    for val in values:
                        #print(val)
                        createIngrediant(recette, key, val)
            else :
                for ele in ingrediants:
                    for o in ele:
                        #print(o)
                        createIngrediant(recette, 'Over All', o)

            #Create instances of Etape
            for ele in obj['steps']:
                #print(ele)
                createEtape(recette, ele)
            
            #Create instances of Information
            for ele in obj['infos']:
                keys = list(ele.keys())
                #print(type(keys))
                key = keys[0]
                value = ele[key]
                #print('key : {key} , value : {value}'.format(key=key, value=value))
                createInformation(recette, key, value)

            #Create or get Personne plus creating the association with recipe
            for ele in obj['reviews']:
                commentaire = ele['comment']
                note = int(ele['note'])
                personne = getOrCreatePersonne(ele['user'])
                createAssosiationCommentaire(recette, personne, commentaire, note)
