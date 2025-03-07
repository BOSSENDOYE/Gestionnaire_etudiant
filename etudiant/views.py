# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant
from .form import EtudiantForm

# Afficher la liste des étudiants
def etudiant_list(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiant/etudiant_list.html', {'etudiants': etudiants})

# Ajouter ou modifier un étudiant
def etudiant_form(request, id=None):
    if id:
        etudiant = get_object_or_404(Etudiant, id=id)
    else:
        etudiant = None
    
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant_list')  # Redirection vers la liste après l'enregistrement
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'etudiant/etudiant_form.html', {'form': form})

# Supprimer un étudiant
def etudiant_delete(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        etudiant.delete()
        return redirect('etudiant_list')
    return render(request, 'etudiant/etudiant_delete.html', {'etudiant': etudiant})

def index(request):
    return render(request, 'etudiant/index.html')