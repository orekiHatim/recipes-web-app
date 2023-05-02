from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def list_recette( request):

    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    recettes = Recette.objects.all()
    print(recettes)
    return render(request,'recettes.html', {'recettes':recettes})

def create_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recettes')

    else:
        form = RecetteForm()
    return render(request ,'create_recette.html',{'form' : form})

def delete_recette(request,pk):
    recette = get_object_or_404(Recette,pk=pk)
    recette.delete()
    return redirect('recettes')

def update_recette(request,pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = RecetteForm(request.POST,instance=recette)
        if form.is_valid():
            form.save()
            return redirect('recettes')

    else:
        form = RecetteForm()
    return render(request ,'update_recette.html',{'form' : form,'recette':recette})

def list_personne(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    #print("hellooooooooooooooooooooooo")
    personnes = Personne.objects.all()
    print(personnes)
    return render(request,'personnes.html', {'personnes': personnes})

def create_personne(request):
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personnes')
    else:
        form = PersonneForm()
        per = Personne.objects.all()
    return render(request ,'create_personne.html',{'form' : form ,'per' : per})

def delete_personne(request,pk):
    personne = get_object_or_404(Personne,pk=pk)
    personne.delete()
    return redirect('personnes')

def update_personne(request,pk):
    personne = get_object_or_404(Personne, pk=pk)
    if request.method == 'POST':
        form = PersonneForm(request.POST,instance=personne)
        if form.is_valid():
            form.save()
            return redirect('personnes')
    else:
        form = PersonneForm()
    return render(request ,'update_personne.html',{'form' : form,'personne':personne})