from django import forms
from .models import *

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre','temps_preparation','etapes']

        widgets = {
            'titre':forms.TextInput(attrs ={'class': 'form-control mb-2'}),

        }
class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['libelle']

        widgets = {
            'libelle':forms.TextInput(attrs ={'class': 'form-control mb-2'}),

        }
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['valeur']

        widgets = {
            'valeur':forms.NumberInput(attrs ={'class': 'form-control mb-2'}),

        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url']

        widgets = {
            'url':forms.TextInput(attrs ={'class': 'form-control mb-2'}),

        }