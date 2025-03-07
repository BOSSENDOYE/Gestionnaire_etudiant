
from django.urls import path
from . import views
from .views import etudiant_form, etudiant_delete, etudiant_list,index



# Exemple de vues

urlpatterns = [
    path('', etudiant_list, name='etudiant_list'),
    path('etudiant/new/', etudiant_form, name='etudiant_create'),
    path('etudiant/<int:id>/edit/', etudiant_form, name='etudiant_edit'),
    path('etudiant/<int:id>/delete/', etudiant_delete, name='etudiant_delete'),
]
