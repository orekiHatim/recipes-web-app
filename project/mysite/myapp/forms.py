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
            'nom' : forms.TextInput(attrs={'class':'form-control'}),
            'prenom' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }