from django.db import models

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def check_password(self, password):
        return self.password == password

class ProfileUtilisateur(Personne):
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)


class Tag(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle


class Recette(models.Model):
    titre = models.CharField(max_length=50)
    temps_preparation = models.IntegerField()
    etapes = models.TextField()
    tag = models.ForeignKey( Tag ,on_delete=models.CASCADE )
    commentaires = models.ManyToManyField(Personne, through='AssociationCommentaire')
    images = models.ManyToManyField('Image')


    def __str__(self):
        return self.titre

class Image(models.Model):
    url = models.CharField(max_length=100)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    recette = models.ManyToManyField(Recette)

    def __str__(self):
        return self.name

class Note(models.Model):
    valeur = models.IntegerField()

class Commentaire(models.Model):
    contenu = models.TextField()

class AssociationCommentaire(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.personne.nom}'s comment on {self.recette.title}"

