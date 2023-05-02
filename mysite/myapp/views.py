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
            return redirect('/recettes')

    else:
        form = RecetteForm()
    return render(request ,'create_recette.html',{'form' : form})

def delete_recette(request,pk):
    recette = get_object_or_404(Recette,pk=pk)
    recette.delete()
    return redirect('/recettes')

def update_recette(request,pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = RecetteForm(request.POST,instance=recette)
        if form.is_valid():
            form.save()
            return redirect('/recettes')

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
    return render(request ,'create_personne.html',{'form' : form})

def delete_personne(request,pk):
    personne = get_object_or_404(Personne,pk=pk)
    personne.delete()
    return redirect('/personnes')

def update_personne(request,pk):
    personne = get_object_or_404(Personne, pk=pk)
    if request.method == 'POST':
        form = PersonneForm(request.POST,instance=personne)
        if form.is_valid():
            form.save()
            return redirect('/personnes')
    else:
        form = PersonneForm()
    return render(request ,'update_personne.html',{'form' : form,'personne':personne})



def list_tag(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    #print("hellooooooooooooooooooooooo")
    tags = Tag.objects.all()
    print(tags)
    return render(request,'tags.html', {'tags': tags})

def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tags')
    else:
        form = TagForm()
    return render(request ,'create_tag.html',{'form' : form})

def delete_tag(request,pk):
    tag = get_object_or_404(Tag,pk=pk)
    tag.delete()
    return redirect('/tags')

def update_tag(request,pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            return redirect('/tags')
    else:
        form = TagForm()
    return render(request ,'update_tag.html',{'form' : form,'tag':tag})


def list_note(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    #print("hellooooooooooooooooooooooo")
    notes = Note.objects.all()
    print(notes)
    return render(request,'notes.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/notes')
    else:
        form = NoteForm()
    return render(request ,'create_note.html',{'form' : form})

def delete_note(request,pk):
    note = get_object_or_404(Note,pk=pk)
    note.delete()
    return redirect('/notes')

def update_note(request,pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('/notes')
    else:
        form = NoteForm()
    return render(request ,'update_note.html',{'form' : form,'note':note})

def list_image(request):
    """""
    for i in range(10):
        Recette(None,f.titre(),f. temps_preparation(),f.etapes(),).save()
   """
    #print("hellooooooooooooooooooooooo")
    images = Image.objects.all()
    print(images)
    return render(request,'images.html', {'images': images})

def create_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/images')
    else:
        form = ImageForm()
    return render(request ,'create_image.html',{'form' : form})

def delete_image(request,pk):
    image = get_object_or_404(Note,pk=pk)
    image.delete()
    return redirect('/images')

def update_image(request,pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST,instance=image)
        if form.is_valid():
            form.save()
            return redirect('/images')
    else:
        form = ImageForm()
    return render(request ,'update_image.html',{'form' : form,'image':image})
