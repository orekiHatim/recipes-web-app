from ..models import Tag, Personne, Recette

def getOrCreateTag(tag):
    tags = Tag.objects.filter(libelle=tag)
    if len(tags) == 0 :
        tag = Tag(libelle=tag)
        tag.save()
        return tag
    return tags[0]


def getOrCreatePersonne(username):
    personnes = Personne.objects.filter(nom=username)
    if len(personnes) == 0:
        personne = Personne(nom=username, prenom='Unknown', email='{}@gmail.com'.format(username), password=username)
        personne.save()
        return personne
    return personnes[0]


def getOrCreateRecette(title, desc, categoryName):
    category = getOrCreateTag(categoryName)
    recettes = Recette.objects.filter(titre=title, description=desc, tag__pk=category.pk)
    if len(recettes) == 0:
        recette = Recette(titre=title, description=desc, tag=category)
        recette.save()
        return recette
    return None

