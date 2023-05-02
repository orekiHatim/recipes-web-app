from django.urls import path
from .views import *

urlpatterns = [
    path('recettes/', list_recette , name='recette'),
    path('recettes/create/', create_recette , name='create_recette'),
    path('recettes/delete/<int:pk>', delete_recette, name='delete_recette'),
    path('recettes/update/<int:pk>', update_recette, name='update_recette'),
    path('personnes/', list_personne, name='personne'),
    path('personnes/create/', create_personne, name='create_personne'),
    path('personnes/delete/<int:pk>', delete_personne, name='delete_personne'),
    path('personnes/update/<int:pk>', update_personne, name='update_personne'),
    path('tags/', list_tag, name='tag'),
    path('tags/create/', create_tag, name='create_tag'),
    path('tags/delete/<int:pk>', delete_tag, name='delete_tag'),
    path('tags/update/<int:pk>', update_tag, name='update_tag'),
    path('notes/', list_note, name='tag'),
    path('notes/create/', create_note, name='create_note'),
    path('notes/delete/<int:pk>', delete_note, name='delete_note'),
    path('notes/update/<int:pk>', update_note, name='update_note'),
    path('images/', list_image, name='tag'),
    path('images/create/', create_image, name='create_image'),
    path('images/delete/<int:pk>', delete_image, name='delete_image'),
    path('images/update/<int:pk>', update_image, name='update_image')
]
