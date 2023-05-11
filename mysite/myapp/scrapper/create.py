from ..models import Image, Etape, Ingredient, Information, AssociationCommentaire

def createImage(rec, name):
    image = Image(url=name, recette=rec)
    image.save()

def createIngrediant(rec, nom, text):
    ingrediant = Ingredient(text=text, name=nom, recette=rec)
    ingrediant.save()

def createEtape(rec, name):
    etape = Etape(text=name, recette=rec)
    etape.save()

def createInformation(rec, k, val):
    info = Information(key=k, value=val, recette=rec)
    info.save()

def createAssosiationCommentaire(rec, per, comment, no):
    association = obj = AssociationCommentaire(personne=per, recette=rec, commentaire=comment, note=no)
    association.save()