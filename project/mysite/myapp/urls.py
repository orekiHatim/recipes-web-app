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
    path('personnes/update/<int:pk>', update_personne, name='update_personne')
]
